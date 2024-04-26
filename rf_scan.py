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

try:
    # 초기 상태와 변화 감지
    initial_state = read_signal()
    print("Initial pin state:", initial_state)
    while True:
        current_state = read_signal()
        if current_state != initial_state:
            print(f"State changed to {current_state}")
            break
        time.sleep(0.1)
finally:
    # GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
