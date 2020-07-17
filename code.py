from adafruit_circuitplayground import cp

import supervisor
import time
import sys
import random

def non_blocking_read():
    rgb_s = []
    s = ""
    while supervisor.runtime.serial_bytes_available and s != '\n':
        s = sys.stdin.read(1)
        rgb_s.append(s)
    return ''.join(rgb_s).strip()

def parse_inp(s):
    return [tuple(int(p) for p in t.split(' ')) for t in s.split(',')]

def light_up(rgb_out):
    # TODO: Varying brightness
    cp.pixels.brightness = 0.01
    cp.pixels[:] = rgb_out

def ran():
    return random.randint(0,255)

def random_rgb():
    return ','.join([
        ' '.join(str(ran())
        for _ in range(3))
        for x in range(10)
    ])

while True:
    # print('circuit-cinema')
    #light_up(parse_inp((random_rgb())))
    # time.sleep(0.5)
    output = non_blocking_read()
    if output:
        print(repr(output), end='-------')
        light_up(parse_inp((output)))
