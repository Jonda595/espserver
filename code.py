from machine import Pin
import time

but = Pin(5, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

while True:
    val = but.value()
    
    if val == 1:
        led.off()
    elif val == 0:
        led.on()
    
    time.sleep(0.1)
