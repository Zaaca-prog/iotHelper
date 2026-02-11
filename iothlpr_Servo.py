from typing import Self
from machine import Pin,PWM 
class Servo():
    def __init__(self, pin:Pin = None, Freq:int = 50, max_angle:int=180) -> None:
        self.pwm = None
        if pin != None:
            self.pwm = PWM(pin)
            self.pwm.freq(Freq)
            self.pwm.duty(0)
        self.max_angle = max_angle
        self.angle = self.pwm.duty()/1023 * 180
    def write_angle(self, angle):
        try:
            self.pwm.duty(int(angle/self.max_angle*1023))
        except OSError:
            print("cannot write angle (may be deinitialized currently)")

    def attach(self,pin:Pin) -> None:
        self.pwm = PWM(pin)
        self.pwm.freq(50)
        self.pwm.duty(0)
    def detach(self) -> None:
        if not isinstance(self.pwm,PWM):
            print(f"Error: Invalid data type. Expected PWM, got {type(self.pwm).__name__}.", file=sys.stderr)
        else:
            self.pwm.deinit()
