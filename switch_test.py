import RPi.GPIO as GPIO
import time
import keyboard

btnPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(btnPin, GPIO.RISING, bouncetime=100)
    # time.sleep(0.1)
    #print(GPIO.input(btnPin))
    if GPIO.input(btnPin) == 0:
        print("switch pushed")

    key = keyboard.read_key()
    if key in ["q", "Q"]:
        break
