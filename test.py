from machine import Pin
import utime

# GPIO 설정
data_pin_out = Pin(27, Pin.OUT)  # 송신 데이터 핀

# 발신 신호
constant_signal = '10111001'

# 송신 함수
def send_signal():
    print("Continuously sending signal: 10111001")
    while True:
        for bit in constant_signal:
            data_pin_out.value(int(bit))
            utime.sleep(0.1)  # 각 비트 전송 지연 시간
        utime.sleep(2)  # 다음 신호 전송 전에 간격을 줍니다

# 메인 루프
try:
    send_signal()
except KeyboardInterrupt:
    print("Program interrupted")
finally:
    print("Clean up and exit")
