"""Fake gpiozero module to shut up the LSP server when developing.
I Should move to an emulator, indeed.
"""


class Button:
    def __init__(self, gpiopin: int) -> None:
        self.gpiopin = gpiopin

    def when_pressed(self):
        pass

    def when_released(self):
        pass

    def wait_for_press(self):
        pass
