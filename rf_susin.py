import lgpio
import time

# GPIO 칩 핸들 설정
h = lgpio.gpiochip_open(0)

# 입력 핀 설정
INPUT_PIN = 27
lgpio.gpio_claim_input(h, INPUT_PIN)

# LED 핀 설정
led_pins = {
    '00': 5,  # 발광색 LED
    '01': 6,  # 초록색 LED
    '10': 13, # 노랑색 LED
    '11': 19  # 파랑색 LED
}

for pin in led_pins.values():
    lgpio.gpio_claim_output(h, pin)

current_signal = ""
last_time = time.time()

try:
    while True:
        bit = lgpio.gpio_read(h, INPUT_PIN)
        current_signal += str(bit)
        # 신호의 끝을 구분하는 조건
        if time.time() - last_time > 0.2:
            if current_signal in led_pins:
                # 현재 LED 상태를 반전
                current_state = lgpio.gpio_read(h, led_pins[current_signal])
                lgpio.gpio_write(h, led_pins[current_signal], not current_state)
                # LED 상태가 토글될 때 메시지 출력
                print(f"LED on pin {led_pins[current_signal]} toggled to {'on' if not current_state else 'off'}.")
            current_signal = ""
            last_time = time.time()
except KeyboardInterrupt:
    # Ctrl+C를 누르면 실행 종료 및 GPIO 칩 핸들 닫기
    lgpio.gpiochip_close(h)
