import random
import serial 
import time
from stream_screen import stream_avg_pixels


SERIAL_PATH = '/dev/ttyACM3'
BAUDRATE = 115200
TIMEOUT = 0.01
FPS = 100

def random_rgb():
    return ','.join(
        [
            ' '.join(str(random.randint(0, 255)) for _ in range(3))
            for _ in range(10)
        ]
    )

def encode_rgb(frame):

    return ','.join([       
        ' '.join(str(int(color)) for color in pixel)
        for pixel in frame
    ])


def send_serial_rgb():
    ser = serial.Serial(SERIAL_PATH, baudrate=BAUDRATE, timeout= TIMEOUT)
    streamer = stream_avg_pixels()
    
    for frame in streamer:
        encoded_frame = encode_rgb(frame) 
        print(f'{encoded_frame=}, {random_rgb()=}')
        out = bytes(encoded_frame, 'utf-8')
        # out = bytes(random_rgb(), 'utf-8')
        ser.write(out + b'\n')  # block
        # print(repr(out))
        # time.sleep(1/FPS)


if __name__ == '__main__':
    send_serial_rgb()