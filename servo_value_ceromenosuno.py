import gpiozero as gp
import time as t

servo = gp.Servo(17)

while True:
    servo.value = 0
    t.sleep(1)
    servo.value = -1
    t.sleep(1)