print("hello world")

import time, sys, math
from grove.adc import ADC

__all__ = ["GroveWaterSensor"]

class GroveWaterSensor:
    '''
    Grove Water Sensor class
    Args:
        pin(int): number of analog pin/channel the sensor connected.
    '''
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        '''
        Get the water strength value
        Returns:
            (int): ratio, 0(0.0%) - 1000(100.0%)
        '''
        return self.adc.read(self.channel)

Grove = GroveWaterSensor


def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = sh.argv2pin()

    sensor = GroveWaterSensor(pin)

    print('Detecting ...')
    while True:
        value = sensor.value
        if sensor.value > 800:
            print("{}, Detected Water.".format(value))
        else:
            print("{}, Dry.".format(value))

        time.sleep(.1)

if __name__ == '__main__':
    main()

