"""
@Project ：new_fms_test
@File    ：chuankou_test.py
@IDE     ：PyCharm
@Author  ：FMS
@Date    ：2023/8/2 19:48
@Des     ：
"""
import binascii
import struct
import time
import serial#导入串口通信库
from time import sleep
import numpy as np


ser = serial.Serial()
def port_open_recv():#对串口的参数进行配置
    ser.port='com5'
    # ser.baudrate=460800
    ser.baudrate = 460800
    ser.bytesize=8
    ser.stopbits=1
    ser.parity="N"#奇偶校验位
    ser.open()
    if(ser.isOpen()):
        print("串口打开成功！")
    else:
        print("串口打开失败！")
#isOpen()函数来查看串口的开闭状态


def port_close():
    ser.close()
    if(ser.isOpen()):
        print("串口关闭失败！")
    else:
        print("串口关闭成功！")

def send(send_data):
    if(ser.isOpen()):
        ser.write(send_data.encode('utf-8'))#编码
        print("发送成功",send_data)
    else:
        print("发送失败！")

def recv(size):
    if(ser.isOpen()):
        data = ser.read(size)
        print('收取成功，{}'.format(data.hex()))
        return data.hex()


def parse_press_data(data):
    data = bytes.fromhex(data)
    data_matrix = zip(*(iter(data),) * 320)
    print(data_matrix)
    data_matrix = [list(i) for i in data_matrix]
    print(data_matrix)
    press_matrix = np.zeros((32, 64))
    print(press_matrix)
    for i in range(20, 80):
        col = 0
        for j in range(80, 320, 4):
            point_bytes = '{:02x}'.format(data_matrix[i][j]) + '{:02x}'.format(data_matrix[i][j + 1]) + '{:02x}'.format(data_matrix[i][j + 2]) + '{:02x}'.format(data_matrix[i][j + 3])
            [point] = struct.unpack('<f', bytes.fromhex(point_bytes))
            press_matrix[i-20][col] = point / 4
            col += 1
    return press_matrix




def my_parse_press_data(data):
    # bin_str = binascii.unhexlify(data)
    bin_str = bytes.fromhex(data)
    matrix = []
    for row in range(64):
        row_data = []
        for col in range(32):
            byte_data = bin_str[col*64 + row:col*64 + row+1].hex()
            # print(bytes.fromhex(byte_data))
            value = struct.unpack('<B',bytes.fromhex(byte_data))[0]
            row_data.append(value)
        matrix.append(row_data)
    print(matrix)
    return matrix


def parse_press_fulll_rt(data):
    bin_str = bytes.fromhex(data)
    matrix = np.zeros((64,32))
    for row in range(64):
        for col in range(32):
            byte_data = bin_str[col*64 + row:col*64 + row+1].hex()
            value = struct.unpack('<B',bytes.fromhex(byte_data))[0]
            matrix[row][col] = value
    return matrix


def parse_press_60_32_rt(data):
    bin_str = bytes.fromhex(data)
    press_matrix = np.zeros((60, 32))
    for row in range(60):
        for col in range(32):
            hex_data = bin_str[col*64 + row+4]
            value = hex_data
            press_matrix[row][col] = value
    return press_matrix

def test_method(data):
    print("1:------"+data)
    bin_str = bytes.fromhex(data)
    print(bin_str)
    for i in bin_str:
        print(i)


if __name__ == '__main__':
    port_open_recv()
    pre_head = '00'
    tail_head = '00'
    is_ready = False
    while not is_ready:
        pre_head = recv(1)
        if pre_head == 'a5':
            tail_head =recv(1)
            if tail_head == '5a':
                is_ready =True
            print(f'1:{pre_head},2:{tail_head}')
        #起到一个延时的效果，这里如果不加上一个while True，程序执行一次就自动跳出了
    other = recv(4)
    data = recv(2048)   #数据帧总长度为2056 = 2048 + 2 + 2 + 1 + 1 + 2
    cal_sum = recv(2)
    press_matrix_1 = parse_press_fulll_rt(data)
    press_matrix_2 = parse_press_60_32_rt(data)
    print(press_matrix_1,'\n', press_matrix_2)






