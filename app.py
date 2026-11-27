import tkinter as tk
from flashing_led import FlashingLED


class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("LED Controller")
        self.root.geometry("300x100")

        self.led = FlashingLED(17, root)

        tk.Button(
            root,
            text="Start",
            command=self.led.start
        ).pack(pady=5)

        tk.Button(
            root,
            text="Stop",
            command=self.led.stop
        ).pack(pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def close_app(self):
        self.led.close()
        self.root.destroy()