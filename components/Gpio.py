# import RPi.GPIO as GPIO
# import time

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)

class Gpio:
  'Common base class for all GPIOS'

  def __init__(self, position, name):
    # GPIO.setup(position, GPIO.OUT)
    self.name = name
    self.position = position

  def on(self):
    # GPIO.output(self.position,GPIO.LOW)
    print("Turned on the", self.name)

  def off(self):
    # GPIO.output(self.position,GPIO.HIGH)
    print("Turned off the", self.name)
