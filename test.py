from gpiozero import LED
from time import sleep

led = LED(27)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
except KeyboardInterrupt:  # Ctrl+C를 누르면 예외 발생
    GPIO.cleanup()  # GPIO 설정 초기화

