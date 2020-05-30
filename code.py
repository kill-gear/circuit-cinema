from adafruit_circuitplayground import cp

import supervisor
import time
import sys

def non_blocking_read():
    i = ""
    while supervisor.runtime.serial_bytes_available:
        i += sys.stdin.read(1)
    return i


while True:
    time.sleep(1)
    if cp.button_a:
        res = non_blocking_read()
        print("Button A pressed!")
        print('result:', res)