import lgpio as GPIO
import time

LED_PIN = 27

# GPIO 핀 설정
GPIO.set_mode(LED_PIN, GPIO.OUTPUT)

try:
    while True:
        # LED 켜기
        GPIO.write(LED_PIN, 1)
        time.sleep(1)
        # LED 끄기
        GPIO.write(LED_PIN, 0)
        time.sleep(1)
except KeyboardInterrupt:
    # 프로그램 종료 시 GPIO 설정 초기화
    GPIO.cleanup()
