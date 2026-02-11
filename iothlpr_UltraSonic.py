from machine import Pin,time_pulse_us import utime class UltraSonic(): def __init__(self, trigpin ,echopin) -> None: self.echo_pin = echopin self.trig_pin = trigpin self.trigger = Pin(trigpin,Pin.OUT)
class UltraSonic():
    def __init__(self,trig:Pin,echo:Pin):
        self.trig_pin = trig
        self.echo_pin = echo 
    def get_cm(self) -> float:
        self.trig_pin.value(0) 
        utime.sleep_us(2)
        self.trig_pin.value(1)
        utime.sleep_us(10)
        self.trig_pin.value(0)
            
        duration = time_pulse_us(self.echo_pin,1,3000)
        cm = duration * 0.0343 / 2 # gets cm
        return cm
    def get_inches(self) -> float:
        self.trig_pin.value(0) 
        utime.sleep_us(2)
        self.trig_pin.value(1)
        utime.sleep_us(10)
        self.trig_pin.value(0)
            
        duration = time_pulse_us(self.echo_pin,1,3000)
        inches = duration * 0.0343 *2.54 / 2 # gets cm
        return inches
    def get_meters(self) -> float:
        self.trig_pin.value(0) 
        utime.sleep_us(2)
        self.trig_pin.value(1)
        utime.sleep_us(10)
        self.trig_pin.value(0)
            
        duration = time_pulse_us(self.echo_pin,1,3000)
        meters = duration * 0.0343 / 200  # gets meters 200 = x/100/2
        return  meters
