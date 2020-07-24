import random
import serial 
import time
from stream_screen import stream_avg_pixels
from hypothesis import given, strategies as st


SERIAL_PATH = '/dev/ttyACM0'
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


def parse_inp(s):
    if not s:
        return []
    return [tuple(int(p) for p in t.split(' ')) for t in s.split(',')]


rgb_val = st.integers(min_value=0, max_value=255)
frames = st.lists(st.tuples(rgb_val, rgb_val, rgb_val), min_size=0)

@given(frames)
def test_encode_decode(frame):
    encoded = encode_rgb(frame)
    decoded = parse_inp(encoded)
    assert decoded == frame 


if __name__ == '__main__':
    send_serial_rgb()

