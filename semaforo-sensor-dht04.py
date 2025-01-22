from machine import Pin, time

# Define los pines
PIN_TRIG = 15
PIN_ECHO = 4
LED_5CM = 17
LED_10CM = 5
LED_15CM = 18

# Configura los pines
trigger = Pin(PIN_TRIG, Pin.OUT)
echo = Pin(PIN_ECHO, Pin.IN)
led_5cm = Pin(LED_5CM, Pin.OUT)
led_10cm = Pin(LED_10CM, Pin.OUT)
led_15cm = Pin(LED_15CM, Pin.OUT)

def get_distance():
  """Mide la distancia con el sensor ultrasónico."""
  trigger.low()
  time.sleep_us(2)
  trigger.high()
  time.sleep_us(10)
  trigger.low()
  while echo.value() == 0:
    pass
  start = time.ticks_us()
  while echo.value() == 1:
    pass
  end = time.ticks_us()
  duration = end - start
  distance = (duration * 0.0343) / 2
  return distance

while True:
  distance = get_distance()
  print("Distancia:", distance, "cm")

  if distance < 5:
    led_5cm.on()    # Enciende LED para 5 cm
    led_10cm.off()   # Apaga los otros LEDs
    led_15cm.off()
  elif distance < 10:
    led_10cm.on()   # Enciende LED para 10 cm
    led_5cm.off()    # Apaga los otros LEDs
    led_15cm.off()
  elif distance < 15:
    led_15cm.on()   # Enciende LED para 15 cm
    led_5cm.off()    # Apaga los otros LEDs
    led_10cm.off()
  else:
    # Si la distancia es mayor a 15 cm, apaga todos los LEDs
    led_5cm.off()
    led_10cm.off()
    led_15cm.off()

  time.sleep(1)  # Espera 1 segundo
