from functools import reduce
from time import sleep
from mss.linux import MSS as mss
    


with mss() as sct:
    # Use the 1st monitor
    monitor = sct.monitors[1]
    # Capture a bbox using percent values
    right = monitor["left"] + monitor["width"]
    lower = monitor["top"] + monitor["height"]
    
    bbox = (monitor['left'], monitor['top'], right, lower)
    for _ in range(1):

        # Grab the picture
        #m.width / 10 Using PIL would be something like:
        im = sct.grab(bbox)  # type: ignore
        sleep(0.2)


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
    average_pixel =\
         sum_r / patch_pixels_num, sum_g / patch_pixels_num, sum_b / patch_pixels_num
    averages.append(average_pixel)
