import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
LED_PIN = 12
GPIO.setmode(GPIO.BCM)  # BCM 모드 설정
GPIO.setup(LED_PIN, GPIO.OUT)  # LED_PIN을 출력으로 설정

try:
    while True:  # 무한 루프
        GPIO.output(LED_PIN, GPIO.HIGH)  # LED 켜기
        time.sleep(1)  # 1초 동안 대기
        GPIO.output(LED_PIN, GPIO.LOW)  # LED 끄기
        time.sleep(1)  # 1초 동안 대기
except KeyboardInterrupt:  # Ctrl+C를 누르면 예외 발생
    GPIO.cleanup()  # GPIO 설정 초기화

