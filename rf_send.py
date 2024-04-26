import lgpio
import time

LED_PIN = 17

# GPIO 칩 핸들 생성 및 열기
h = lgpio.gpiochip_open(0)

# GPIO 핀을 출력으로 설정
lgpio.gpio_claim_output(h, LED_PIN)

def send_signal(signal):
    for bit in signal:
        # 신호 전송 (0 또는 1)
        lgpio.gpio_write(h, LED_PIN, int(bit))
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
    # Ctrl+C를 누르면 실행 종료 및 GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
