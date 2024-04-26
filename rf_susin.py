import lgpio
import time

# GPIO 핸들 설정
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
            current_signal = ""
            last_time = time.time()
except KeyboardInterrupt:
    # Ctrl+C를 누르면 GPIO 설정을 정리
    lgpio.gpiochip_close(h)
