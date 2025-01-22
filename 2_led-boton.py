from machine import Pin
import time

led = Pin(25, Pin.OUT)  
boton = Pin(14, Pin.IN, Pin.PULL_DOWN) 

while True:
  if boton.value() == 1:
    led.toggle() 
    time.sleep(0.2)  
