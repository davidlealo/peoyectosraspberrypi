from gpiozero import Servo
from time import sleep
servo = Servo(17)

while True:
    servo.value = 1
    sleep(1)
    servo.value = -1
    sleep(1)