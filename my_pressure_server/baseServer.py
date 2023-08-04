"""
@Project ：new_fms_test
@File    ：baseServer.py
@IDE     ：PyCharm
@Author  ：FMS
@Date    ：2023/8/4 10:25
@Des     ：
"""

import logging
import socket
import sys
import serial
from socket import SocketS

class SocketStatus:
    READY = 0
    RUNNING = 1
    CLOSED = 2

class ScoketServer:
    host = None
    port = None

    def __init__(self, host="127.0.0.1", port=5005):
        self.status = SocketStatus.READY
        self.address = (host, port)
        self.socket_server = socket.scoket(socket.AF_INET, socket.SOCK_STREAM)

