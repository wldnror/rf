import lgpio
import time

LED_PIN = 27

# Handle creation and opening
h = lgpio.gpiochip_open(0)

try:
    # Set the GPIO pin as an output
    lgpio.gpio_claim_output(h, LED_PIN)

    while True:
        # Turn the LED on
        lgpio.gpio_write(h, LED_PIN, 1)
        time.sleep(1)
        # Turn the LED off
        lgpio.gpio_write(h, LED_PIN, 0)
        time.sleep(1)

except KeyboardInterrupt:
    # Cleanup on Ctrl+C
    lgpio.gpiochip_close(h)
