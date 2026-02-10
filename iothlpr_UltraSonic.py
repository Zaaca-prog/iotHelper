from machine import Pin,time_pulse_us
import utime
class UltraSonic():
    def __init__(self, trigpin ,echopin) -> None:
        self.echo_pin = echopin
        self.trig_pin = trigpin
        self.trigger = Pin(trigpin,Pin.OUT)
    def get_cm(self) -> float:
        self.trigger.value(0) 
        utime.sleep_us(2)
        self.trigger.value(1)
        utime.sleep_us(10)
        self.trigger.value(0)
            
        duration = time_pulse_us(self.echo_pin,1,3000)
        cm = duration * 0.0343 / 2 # gets cm
        return cm 
