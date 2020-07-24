from functools import reduce
from time import sleep
from mss.linux import MSS as mss    
import numpy as np


def calc_avg_pixels_np(im, m=2, n=5):
    np_pixels_arr = np.array(im.pixels)
    height, width , _ = np_pixels_arr.shape
    np_pixels_avg = np_pixels_arr.reshape(m * n, height // m, width // n, 3)
    np_pixels_avg = np.mean(np_pixels_avg, axis=(1,2))
    return np_pixels_avg.tolist()


def calc_avg_pixels(im, m=1, n=10):
    #TODO: Optimise calculation
    averages = []
    NUM_BLOCKS = 10
    height = im.size.height // NUM_BLOCKS
    patch_pixels_num = height * im.size.width
    for i in range(NUM_BLOCKS):
        patch = im.pixels[i*height:(i+1)*height]
        sum_r, sum_g, sum_b = reduce(
            lambda p1, p2: [p1[0]+p2[0], p1[1]+p2[1], p1[2]+p2[2]],
            [pixel for row in patch for pixel in row]
            )
        average_r = sum_r / patch_pixels_num
        average_g = sum_g / patch_pixels_num
        average_b = sum_b / patch_pixels_num
        averages.append([average_r, average_g, average_b])
    return averages
im = []
def stream_avg_pixels():
    
    with mss() as sct:
        # Use the 1st monitor
        monitor = sct.monitors[1]
        # Capture a bbox using percent values
        right = monitor["left"] + monitor["width"]
        lower = monitor["top"] + monitor["height"]
        
        bbox = (monitor['left'], monitor['top'], right, lower)
        while True:


            # Grab the picture
            #m.width / 10 Using PIL would be something like:
            im = sct.grab(bbox)  # type: ignore
            # return im
            yield calc_avg_pixels_np(im)
            
# im = stream_avg_pixels()


