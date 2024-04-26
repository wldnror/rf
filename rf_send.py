import lgpio
import time

LED_PIN = 17  # 발신 핀 번호 설정

# GPIO 칩 핸들 생성 및 열기
h = lgpio.gpiochip_open(0)

# GPIO 핀을 출력으로 설정
lgpio.gpio_claim_output(h, LED_PIN)

def send_signal(signal):
    while True:  # 무한 루프를 추가하여 계속해서 신호를 보냄
        for bit in signal:
            # 신호 전송 (0 또는 1)
            lgpio.gpio_write(h, LED_PIN, int(bit))
            time.sleep(0.1)  # 각 비트 사이의 딜레이

try:
    # 신호를 계속 전송
    send_signal('01110110')
except KeyboardInterrupt:
    # 사용자가 Ctrl+C를 누르면 루프를 중단
    print("신호 전송 중단")
finally:
    # GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
