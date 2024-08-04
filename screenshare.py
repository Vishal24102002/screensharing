""" screenshare-share: Python module for Sharing your screen over same network as video (without sound) over same network
Copyright © 2024 Coder-wis <vishalsharma.pypi@gmail.com>
Released under the terms of the MIT license (https://opensource.org/licenses/MIT) as described in LICENSE.md
"""
import time
import cv2
from mss import mss
import pyautogui
import socket
import numpy as np
from colorama import Fore

print(f"{Fore.RED}-------------------------Thanks for using our product-----------------------{Fore.WHITE}")


class server:
    """
        Main class of server. Handles loading and sending
        the screen inside the selected window.

        :keyword host:
            host ip address from the sender side
        :keyword size:
            size os the screen to be shared
            by default it takes the entier screen of the pc
        :param port:
            it contains the port number which is used for sending file,
            if not it uses port-9999 as a default
        :param noofconn:
            it stands for number of connections
            default value is 1
    """

    def __init__(self,host,port=8080,noofconn=1,video_frame=True):
        self.host=host
        self.port=port
        self.noofconn=noofconn
        self.video_frame=video_frame

    def create(self):
        self.create_server(self.port,self.noofconn)

    def create_server(self,port,noofconn):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("Socket successfully created")
        host=socket.gethostname()
        print("host name ->", host)
        server.bind((host,port))
        server.listen(noofconn)
        print("waiting for connections ....")
        server_client,addr=server.accept()
        print(addr,"connected sucessfully")
        print("list of devices --> ",server_client)
        self.sending(server,server_client,self.noofconn)

    def sending(self,server,server_client,noofconn):
        with server_client:
            while True:
                scr_width, scr_height=pyautogui.size()
                bounding_box = {'top': 0, 'left': 0, 'width':scr_width, 'height':scr_height}
                sct=mss()
                sct_img = sct.grab(bounding_box)
                frame=np.array(sct_img)

                # Encode the frame as a JPEG
                _, buffer = cv2.imencode('.jpeg', frame)
                frame_data = buffer.tobytes()

                # Send the frame size
                frame_size = len(frame_data)
                server_client.sendall(frame_size.to_bytes(4, byteorder='big'))
                # Send the frame data
                server_client.sendall(frame_data)

                # server_client.sendall(frame)
                if not self.video_frame:
                    break


class server_receive:

    def __init__(self,host,port=8090,display=True,video=True):
        self.host=host
        self.port=port
        self.display=display
        self.video=video

    def connect(self):
        self.connect_rec(self.host,self.port)

    def connect_rec(self,host,port):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.connect((host,port))
        print("Connected to the Host")
        self.Recei(client)

    def Recei(self,client):
        cv2.namedWindow("Screen Share", cv2.WINDOW_AUTOSIZE)
        while True:
            frame_size = client.recv(4)
            if not frame_size:
                break
            frame_size = int.from_bytes(frame_size, byteorder='big')
            # Receive the frame data
            frame_data=b''
            while len(frame_data) < frame_size:
                packet = client.recv(frame_size - len(frame_data))
                if not packet:
                    break
                frame_data += packet

            if not frame_data:
                break

            # Decode the frame data
            frame = np.frombuffer(frame_data, dtype=np.uint8)
            frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)

            # Adjust size if necessary

            # Display the frame
            cv2.imshow("Screen Share", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

