import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

led_pins = {
    '00': 5,  # 발광색 LED
    '01': 6,  # 초록색 LED
    '10': 13, # 노랑색 LED
    '11': 19  # 파랑색 LED
}
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)

current_signal = ""
last_time = time.time()

try:
    while True:
        bit = GPIO.input(27)
        current_signal += str(bit)
        if time.time() - last_time > 0.2:  # 신호의 끝을 구분
            if current_signal in led_pins:
                GPIO.output(led_pins[current_signal], not GPIO.input(led_pins[current_signal]))
            current_signal = ""
            last_time = time.time()
except KeyboardInterrupt:
    GPIO.cleanup()
