![Circuit Playground Express](https://cdn-learn.adafruit.com/guides/cropped_images/000/001/799/medium640/cpx01.jpg?1520545756)
# Circuit Cinema

##### Make RGB NeoPixel LEDs on Adafruit [Circuit Playground Express](https://www.adafruit.com/product/3333) glow in sync to host computer's monitor sprucing up your movie / game with fabulous ambient lighting.


## Getting Started

These instructions will get you a copy of the project up and running on your CPX connected to your host machine.

If you're new to CircuitPython or CPX, [start here](https://learn.adafruit.com/adafruit-circuit-playground-express).

### Prerequisites
* Micro B USB connector. Go with the tried and true micro-B USB connector for power and/or USB communication. 

* Circuit Plaground Express flashed with CircuitPython (5.3.0) - [Installing CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)

* This project is built in Python, so make sure Python 3.x is installed on your system. Once Python is installed, create a virtual environment in the root directory of this repo using the following command:

```
    $ python3 -m venv circuit-cinema-venv
```
    Then activate this virtual environment using:
```
    $ source ./circuit-cinema-env/bin/activate (for Windows users this can look like workon circuit-cinema-env, see the relevant virtualenv documentation for exact usage)
```
    Now install the dependencies using the following command:
```
    $ python3 -m pip install -r requirements.txt
```


### Installing

- After installing all the dependencies, connect CPX to computer, the board shows up as a USB drive called CIRCUITPY. The CIRCUITPY drive is where your code and the necessary libraries and files will live.

- CircuitPython looks for `code.py` or  `main.py` files (in this order) and runs the contents of the file automatically when the board starts up, reloads, or when you save changes to the file.

- Next, copy and replace the contents from `code.py` (in this repo) with the one in CIRCUITPY drive and [save.](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code)

- Now run the `./screen_reader.py` (with escalated privileges or as root on *\*nix* OS's and in circuit-cinema-env venv).
    - This will capture your screen, calculate RGB values for NeoPixels, encode them and send them via serial connection using PySerial.

    ```
    source ./circuit-cinema-venv/bin/activate
    ```
    ```
    python3 screen_reader.py
    ```

![Check this out for results](https://www.dl.dropboxusercontent.com/s/qfhtx09l7r5o02e/20200823_215401-ANIMATION.gif?dl=0)
***Voila, enjoy the lightgasm on CPX while you watch a movie.***

***


#### Authors

* **Manan Nahata** - [kill-gear](https://github.com/kill-gear)

* **Saurabh Chaturvedi** - [schedutron](https://github.com/schedutron)

#### License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
