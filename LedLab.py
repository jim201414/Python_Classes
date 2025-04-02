__version__ = '0.1.0'
__author__ = 'Jim Harisis'
__license__ = "Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0"

from telemetrix import telemetrix
from time import sleep
board = telemetrix.Telemetrix()

class LED:

    def __init__(self, pin):
        self.pin = pin
        board.set_pin_mode_digital_output(self.pin)

    def on(self):
        board.digital_write(self.pin, 1)

    def off(self):
        board.digital_write(self.pin, 0)

    def blink(self, times, delay):
        for i in range(times):
            sleep(delay)
            board.digital_write(self.pin, 1)
            sleep(delay)
            board.digital_write(self.pin, 0)
