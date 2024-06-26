import lgpio
import time

LED_PIN = 27  # 수신 핀 번호 설정

# GPIO 칩 핸들 생성 및 열기
h = lgpio.gpiochip_open(0)

# GPIO 핀을 입력으로 설정
lgpio.gpio_claim_input(h, LED_PIN)

try:
    initial_state = lgpio.gpio_read(h, LED_PIN)
    print("Initial pin state:", initial_state)
    
    # 상태 변화 감지를 위한 루프
    while True:
        current_state = lgpio.gpio_read(h, LED_PIN)
        if current_state != initial_state:
            print(f"State changed to {current_state}")
            break
        time.sleep(0.1)
finally:
    # GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
