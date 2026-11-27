from gpiozero import LED

class FlashingLED:
    def __init__(self, pin: int):
        self.led = LED(pin)

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

    def close(self):
        self.led.close()


