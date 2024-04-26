import lgpio
import time

LED_PIN = 27  # 수신 핀 번호 설정

# GPIO 칩 핸들 생성 및 열기
h = lgpio.gpiochip_open(0)

# GPIO 핀을 입력으로 설정
lgpio.gpio_claim_input(h, LED_PIN)

def read_signal():
    # 신호를 읽고 이를 문자열로 반환
    return str(lgpio.gpio_read(h, LED_PIN))

def detect_signal():
    # 특정 신호를 감지하면 출력
    if read_signal() == '1':
        print("Signal detected!")
        return True
    return False

try:
    # 반복해서 신호 감지 시도
    while True:
        if detect_signal():
            break
        time.sleep(0.1)  # 감지 시도 사이의 딜레이
finally:
    # GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
