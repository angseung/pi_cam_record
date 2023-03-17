import time
from datetime import datetime
import RPi.GPIO as GPIO
from picamera2 import Picamera2

btnPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

picam2 = Picamera2()
config = picam2.create_preview_configuration({"size": (1280, 720)})
picam2.configure(config)

picam2.start(show_preview=True)

while True:
    GPIO.wait_for_edge(btnPin, GPIO.RISING, bouncetime=100)
    time.sleep(0.5)
    print(GPIO.input(btnPin))

    if GPIO.input(btnPin) == 0:
        now = str(datetime.now())
        print(f"switch pushed at {now}")
        picam2.capture_file(f"test_{now}.jpg")
        print(f"image saved, {now}")
