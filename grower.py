import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Gpio:
  'Common base class for all GPIOS'

  def __init__(self, position):
    GPIO.setup(position, GPIO.OUT)
    self.position = position

  def getPosition(self):
    print("Position: ",self.position)

  def turnOn(self):
    GPIO.output(self.position,GPIO.LOW)

  def turnOff(self):
    GPIO.output(self.position,GPIO.HIGH)


lights = Gpio(16)

lights.getPosition()
