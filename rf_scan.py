import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

def read_signal():
    # 신호를 읽고 이를 문자열로 반환
    return str(GPIO.input(27))

def detect_repeated_signals(required_repeats=3):
    last_signal = None
    repeat_count = 0
    while True:
        signal = read_signal()
        if signal == last_signal:
            repeat_count += 1
        else:
            repeat_count = 1
            last_signal = signal
        
        if repeat_count >= required_repeats:
            print(f"Repeated signal {signal} detected {repeat_count} times.")
            # 필요한 동작을 실행
            repeat_count = 0  # 카운트를 리셋

try:
    detect_repeated_signals(required_repeats=5)  # 여기서 반복 횟수를 설정
except KeyboardInterrupt:
    GPIO.cleanup()
