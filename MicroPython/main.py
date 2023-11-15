"""
Created by: Michael B
Created on: Nov 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *
from math import *


# SparkFun Electronics
# Experiment 8.0
# Using a servo motor
class Servo:
    def __init__(self, pin, freq=50, min_us=600, max_us=2400, angle=180):
        self.min_us = min_us
        self.max_us = max_us
        self.us = 0
        self.freq = freq
        self.angle = angle
        self.analog_period = 0
        self.pin = pin
        analog_period = round((1 / self.freq) * 1000)  # hertz to miliseconds
        self.pin.set_analog_period(analog_period)

    def write_us(self, us):
        us = min(self.max_us, max(self.min_us, us))
        duty = round(us * 1024 * self.freq // 1000000)
        self.pin.write_analog(duty)
        sleep(1000)
        self.pin.write_digital(0)  # turn the pin off

    def write_angle(self, degrees=None):
        if degrees is None:
            degrees = math.degrees(radians)
        degrees = degrees % 360
        total_range = self.max_us - self.min_us
        us = self.min_us + total_range * degrees // self.angle
        self.write_us(us)


# setup
display.show(Image.HAPPY)

# loop
while True:
    if button_a.is_pressed():
        # turn servo 0 deegres
        Servo(pin14).write_angle(0)
        display.clear()
        display.show("0")
        sleep(1000)
        deegreSign = Image("99900:" "90900:" "99900:" "00000:" "00000")
        display.show(deegreSign)
        sleep(1000)

    if button_b.is_pressed():
        # turn servo 180 deegres
        Servo(pin14).write_angle(180)
        display.clear()
        display.show("180")
        sleep(1000)
        deegreSign = Image("99900:" "90900:" "99900:" "00000:" "00000")
        display.show(deegreSign)
        sleep(1000)
    display.clear()
    display.show(Image.HAPPY)
