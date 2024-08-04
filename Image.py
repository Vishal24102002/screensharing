""" ttkscreen-share: Python module for Sharing your screen over same network as video (without sound) over same network
Copyright © 2024 Coder-wis <vishalsharma.pypi@gmail.com>
Released under the terms of the MIT license (https://opensource.org/licenses/MIT) as described in LICENSE.md
"""

import cv2
from mss import mss
import pyautogui,socket,os
import numpy as np
from colorama import Fore

print(f"{Fore.RED}-------------------------Thanks for using our product-----------------------{Fore.WHITE}")


class server():
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

    def __init__(self,host,port=8080,noofconn=1):
        self.host=host
        self.port=port
        self.noofconn=noofconn

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
        self.sending(server,server_client,self.noofconn)

    def sending(self,server,client,noofconn):
        with client:
            while True:
                data=client.recv(1024).decode()
                print(data)
                client.send("data transfer sucessful".encode())
                scr_width, scr_height=pyautogui.size()
                bounding_box = {'top': 0, 'left': 0, 'width':scr_width, 'height':scr_height}
                sct=mss()
                client.send('received_scr.jpeg'.encode())
                sct_img = sct.grab(bounding_box)
                cv2.imwrite('transfer_scr.jpeg',np.array(sct_img))
                with open('transfer_scr.jpeg','rb') as file:
                    while True:
                        data = file.read(1024)
                        if not data:
                            break
                        client.sendall(data)
                # client.send(b"<COMPLETE>")
                print("File transmitted sucessfully")
                for i in range(noofconn):
                    client[i].close()
                    server.close()
                    print("--> Disconnected...")


class server_receive():

    def __init__(self,host,port=8090):
        self.host=host
        self.port=port

    def connect(self):
        self.connect_rec(self.host,self.port)

    def connect_rec(self,host,port):
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # client.sendto("good task".encode(),(host,port))
        client.connect((host,port))
        print("Connected to the Host")
        try:
            # initial request to check the connection
            client.send("Hello, Server!".encode())
            print(client.recv(1204))
            file_name=client.recv(1204)
            print(f"Received from server: {file_name.decode()}")
            with open(file_name, 'wb') as file:
                while True:
                    data = client.recv(1024)
                    if not data:
                        break
                    file.write(data)
            print("file recevied")
        finally:
            # Close the connection
            client.close()
