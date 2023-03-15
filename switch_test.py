import RPi.GPIO as GPIO
import time

switch = 18

# GPIO.setmode(GPIO.BCM)
#
# GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.add_event_detect(switch, GPIO.FALLING, callback=LED369, bouncetime=300)
# print("Wait for the switch event.")
#
# while True:
#     try:
#         sleep(5)
#     except KeyboardInterrupt:
#         print("Au revoir!".center(20))
#         GPIO.cleanup()
#         break

btnPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(btnPin, GPIO.RISING, bouncetime=100)
    time.sleep(0.1)
    #print(GPIO.input(btnPin))
    if GPIO.input(btnPin) == 0:
        print("switch pushed")
