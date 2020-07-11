import random
import serial 
import time

SERIAL_PATH = '/dev/ttyACM7'
BAUDRATE = 115200
TIMEOUT = 0.01

def random_rgb():
    return ','.join(
        [
            ' '.join(str(random.randint(0, 255)) for _ in range(3))
            for _ in range(10)
        ]
    )

def send_serial_rgb():
    ser = serial.Serial(SERIAL_PATH, baudrate=BAUDRATE, timeout= TIMEOUT)

    while True:
        out = bytes(random_rgb(), 'utf-8')
        ser.write(out + b'\n')  # block
        print(repr(out))
        # time.sleep(1)


if __name__ == '__main__':
    send_serial_rgb()
