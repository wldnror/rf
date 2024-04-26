from rpi_rf import RFDevice
import time

rfdevice = RFDevice(17)  # GPIO 17번 핀을 사용
rfdevice.enable_tx()  # 송신 모드 활성화

code = 5526889  # 전송할 코드 (예시 값)
protocol = 1
pulse_length = 350

try:
    while True:
        rfdevice.tx_code(code, protocol, pulse_length)
        print(f'Code {code} sent')
        time.sleep(1)  # 매초마다 신호 전송
except KeyboardInterrupt:
    print("신호 전송 중단")
finally:
    rfdevice.cleanup()  # 리소스 정리
