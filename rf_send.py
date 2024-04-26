import lgpio
import time

LED_PIN = 17  # 발신 핀 번호 설정

# GPIO 칩 핸들 생성 및 열기
h = lgpio.gpiochip_open(0)

# GPIO 핀을 출력으로 설정
lgpio.gpio_claim_output(h, LED_PIN)

def send_signal(signal):
    for bit in signal:
        # 신호 전송 (0 또는 1)
        lgpio.gpio_write(h, LED_PIN, int(bit))
        time.sleep(0.1)  # 각 비트 사이의 딜레이

# 신호 전송
send_signal('1111')

# GPIO 칩 핸들 닫기
lgpio.gpiochip_close(h)
