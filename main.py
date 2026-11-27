from gpiozero import LED
from time import sleep




class FlashingLED:
    def __init__(self, pin):
        self.led = LED(pin)

    def flash(self):
        self.led.on()
        sleep(0.1)

        self.led.off()
        sleep(0.1)

        self.led.on()
        sleep(0.1)

        self.led.off()
        sleep(0.8)

    def run(self):
        while True:
            self.flash()

led = FlashingLED(17)
led.run()


