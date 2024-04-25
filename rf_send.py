import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

def send_signal(signal):
    for bit in signal:
        GPIO.output(17, int(bit))
        time.sleep(0.1)  # 간단한 딜레이로 비트를 전송합니다.

button_signals = {
    1: '00',
    2: '01',
    3: '10',
    4: '11'
}

try:
    while True:
        input_val = int(input("Enter button number (1-4): "))
        if input_val in button_signals:
            send_signal(button_signals[input_val])
        else:
            print("Invalid button")
except KeyboardInterrupt:
    GPIO.cleanup()
