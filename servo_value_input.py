import gpiozero as gp
import time as t

servo = gp.Servo(17)

message = float(input('Elija una posición del servo entre 1 y -1 '))

print(message)
t.sleep(1)
servo.value = message
t.sleep(1)