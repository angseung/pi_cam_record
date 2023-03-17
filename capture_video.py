import os
import time
import shutil
from datetime import datetime
import RPi.GPIO as GPIO
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

target_dir = "videos"
if not os.path.isdir(target_dir):
    os.makedirs(target_dir, exist_ok = False)

btnPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(btnPin, GPIO.IN, GPIO.PUD_UP)

picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (1280, 720)})
picam2.configure(config)
encoder = H264Encoder(10000000)

picam2.start(show_preview=True)

while True:
    GPIO.wait_for_edge(btnPin, GPIO.RISING, bouncetime=100)
    time.sleep(0.5)
    print(GPIO.input(btnPin))

    if GPIO.input(btnPin) == 0:
        now = str(datetime.now())
        print(f"switch pushed at {now}")
        # output = FfmpegOutput("test.mp4", audio=False)
        # picam2.start_recording(encoder, output)
        picam2.start_and_record_video("test.mp4", duration=5)
        time.sleep(0.5)
        # picam2.stop_recording()
        print(f"video saved, {now}")
        shutil.move("test.mp4", f"{target_dir}/test_{now}.mp4")
        picam2.start(show_preview=True)
