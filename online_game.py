import socket
import socketserver
import time

from config import PROXY_HOST, PROXY_PORT
from src.board import Board
from src.game import place_figure, play_game
from src.online.server import MyTCPHandler

HOST = "0.0.0.0"
PORT = int(input('Enter free port: '))

# print(f'Your addr is {socket.gethostbyname(socket.getfqdn())}:{PORT}')
is_host = input('Are u host? [y/n]: ')

b = Board()
if is_host == 'y':
    color = True
    ip_second = input('Enter ip of second player: ')
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(60 * 60)
            sock.connect((PROXY_HOST, PROXY_PORT))
            quer = f'CHECK;{ip_second}'
            sock.sendall(bytes(quer, 'utf-8'))
            response = sock.recv(1024 * 8)
            response = response.decode('utf-8')
            if 'OK' in response:
                break
            raise socket.error
        except socket.error:
            print(f'Waiting for {ip_second}')
            time.sleep(3)
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(60 * 60)
        sock.connect((PROXY_HOST, PROXY_PORT))
        index, new_index = play_game(b, color)
        quer = f'MOVE;{ip_second};{index};{new_index}'
        sock.sendall(bytes(quer, 'utf-8'))
        response = str(sock.recv(1024), 'utf-8')
        red_ind, red_new = response.split(';')[1], response.split(';')[2]
        place_figure(b, not color, red_ind, red_new)
else:
    color = False
    print('Waiting for connection')
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.color = color
        server.board = b
        server.serve_forever()
