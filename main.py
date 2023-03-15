from picamera2 import Picamera2


picam2 = Picamera2()
picam2.start_and_capture_file("test.jpg")
picam2.start_and_record_video("test.mp4", duration=5)
