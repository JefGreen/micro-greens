# import RPi.GPIO as GPIO
# import time

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)

from components.Gpio import Gpio

lights = Gpio(16,'lights')

lights.turnOff()
