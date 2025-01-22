from machine import SoftSPI, Pin
from max7219 import Matrix8x8
import time

# Definir pines para el SPI
max_clk = const(18)
max_cs = const(5)
max_din = const(23)

# Inicializar el SPI con SoftSPI
spi = SoftSPI(sck=Pin(max_clk), mosi=Pin(max_din), miso=Pin(14))

# Inicializar la matriz MAX7219 (8 dispositivos en cascada para una matriz de 64x8)
display = Matrix8x8(spi, Pin(max_cs), 1)  # 8 módulos en cadena para una matriz 64x8
display.brightness(5)  # Ajustar el brillo

# Función personalizada para desplazar el texto
def scroll_text(text, delay=0.1):
    length = len(text) * 8  # Calcular el tamaño total del texto en píxeles
    for i in range(length + 8):  # Desplazar a través de la matriz
        display.fill(0)  # Limpiar pantalla
        display.text(text, 8 - i, 0, 1)  # Mostrar texto desplazado
        display.show()  # Actualizar pantalla
        time.sleep(delay)
while True:
# Llamar a la función para desplazar el texto
    scroll_text("MicroPython", delay=0.05)
