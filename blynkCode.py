from blynklib import Blynk
import RPi.GPIO as GPIO
import time

# Suppress GPIO warnings
GPIO.setwarnings(False)

BLYNK_AUTH_TOKEN = 'SxJyt2nJ3z87VWSC99xEk3Jl-0XR3ipj'
led1 = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

# Initialize Blynk
blynk = Blynk(BLYNK_AUTH_TOKEN)

def blynk_connected():
    print("Raspberry Pi Connected to Blynk")

try:
    print("Starting Blynk loop")
    while True:
        blynk.run()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Exiting gracefully")
     GPIO.cleanup()