#!/usr/bin/env python3

import os
import serial
import signal
from utils import ser, PATH, gen_folder_name, send_message, receive_message
from time import sleep, time
from picamera import PiCamera
from http.server import BaseHTTPRequestHandler, HTTPServer


host_name = '192.168.1.101'
host_port = 8000
shot_command = False
MASTER_PID = 0


# Initiate the Pi camera
# camera = PiCamera()
# camera.resolution = (3280, 2464)
# # Camera warm-up time
# camera.start_preview()
# sleep(2)


class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
           <html>
           <body 
            style="width:960px; margin: 20px auto;">
           <h1>Welcome to my Raspberry Pi</h1>
           <form action="/" method="POST">
               Turn LED :
               <input type="submit" name="submit" value="start">
               <input type="submit" name="submit" value="update">
               <input type="submit" name="submit" value="stop">
           </form>
           </body>
           </html>
        '''
        self.do_HEAD()
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]


        if post_data == 'start':
            os.kill(MASTER_PID, signal.SIGUSR1)
        elif post_data == 'update':
            print("Update!")
        elif post_data == 'stop':
            print("STOP!")

        self._redirect('/')  # Redirect back to the root url


def create_folder():

    # get the folder name
    folder = gen_folder_name()

    # ask the SLAVE that the name of the folder is the same
    send_message(folder, 'Name of the folder are not the same')

    os.mkdir(PATH+folder)
    return PATH + folder + '/'


def shot(n, folder):
    # MASTER send "n"
    if (n < 10):
        photo = "0%d_ir.jpg" % n
    else:
        photo = "%d_ir.jpg" % n

    print("Going to shot %s" % photo)
    send_message(str(n), 'Photo name not synced')

    # MASTER say the SLAVE to shoot a photo
    send_message("shoot", 'Photo not shooted')
    # camera.capture(folder+photo)

    # Wait the SLAVE to confirm
    receive_message("shooted", 'Photo not shooted')
    print("Shot %d_rgb.png\n" % n)


def handler(signum, frame):
    global shot_command
    shot_command = not shot_command


def master_UART():
    global shot_command
    while True:
        if shot_command:
            send_message("init", 'Error on init message')
            folder = create_folder()
            MAX = 10
            for n in range(MAX):
                sleep(1)
                if shot_command:
                    shot(n+1, folder)
                else:
                    send_message("stop", "Stop message didn't arrived")
                    print("User stopped the shooting")
                    break
            shot_command = False
        else:
            sleep(1)


if __name__ == '__main__':
    serial_master = os.fork()
    signal.signal(signal.SIGUSR1, handler)
    if serial_master == 0:
        master_UART()
    else:
        # global MASTER_PID
        MASTER_PID = serial_master
        http_server = HTTPServer((host_name, host_port), MyServer)
        print("Server Starts - %s:%s" % (host_name, host_port))

        try:
            http_server.serve_forever()
        except KeyboardInterrupt:
            http_server.server_close()

