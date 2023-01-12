from gpiozero import LED
from signal import pause

led = LED(20)

led.blink(1)
pause()