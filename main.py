import time

from SerialOp.SerialOp import SerialeOp

if __name__ == '__main__':
    ser_op = SerialeOp()
    full_data = ser_op.get_all_pressure()
    print(time.time())
    full_data = ser_op.get_all_pressure()
    print(time.time())
    full_data = ser_op.get_all_pressure()
    print(time.time())
    print(full_data)

