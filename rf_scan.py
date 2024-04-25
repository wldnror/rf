import lgpio
import time

LED_PIN = 27

# GPIO 칩 핸들 생성 및 열기
h = lgpio.gpiochip_open(0)

# GPIO 핀을 입력으로 설정
lgpio.gpio_claim_input(h, LED_PIN)

def read_signal():
    # 신호를 읽고 이를 문자열로 반환
    return str(lgpio.gpio_read(h, LED_PIN))

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
    # Ctrl+C를 누르면 실행 종료 및 GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
