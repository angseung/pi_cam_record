import time
from datetime import datetime
import RPi.GPIO as GPIO
from picamera2 import Picamera2

btnPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

picam2 = Picamera2()
picam2.start_preview()

while True:
    GPIO.wait_for_edge(btnPin, GPIO.RISING, bouncetime=100)
    time.sleep(1.0)
    print(GPIO.input(btnPin))

    if GPIO.input(btnPin) == 0:
        print("switch pushed")
        now = str(datetime.now())
        picam2.start_and_capture_file(f"test_{now}.jpg")
