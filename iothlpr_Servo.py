from machine import Pin,PWM
class Servo():
    def __init__(self, pin, Freq, max_angle=180) -> None:
        self.pwm = PWM(pin,freq=Freq)
        self.max_angle = max_angle
    def write_angle(self, angle):
        self.pwm.duty(angle/self.max_angle*1023)

    
