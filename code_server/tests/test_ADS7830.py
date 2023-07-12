import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

#sys.path.append('/home/arau/code_server/')

from ADS7830 import *

import pytest
from unittest.mock import MagicMock
#from my_module import ADS7830

@pytest.fixture
def ads7830():
    return ADS7830()

def test_readAdc(ads7830):
    ads7830.bus.write_byte = MagicMock()
    ads7830.bus.read_byte = MagicMock(return_value=123)
    assert ads7830.readAdc(0) == 123
    ads7830.bus.write_byte.assert_called_once_with(0x48, 0x84)

def test_voltage_battery1_first_time(ads7830):
    ads7830.readAdc = MagicMock(return_value=100)
    battery1, _ = ads7830.batteryPower()
    assert battery1 == 3.92
    assert ads7830.battery1Voltage == [100] * 25

def test_voltage_battery2_first_time(ads7830):
    ads7830.readAdc = MagicMock(return_value=150)
    _, battery2 = ads7830.batteryPower()
    assert battery2 == 5.88
    assert ads7830.battery2Voltage == [150] * 25

def test_voltage_battery1_second_time(ads7830):
    ads7830.readAdc = MagicMock(return_value=200)
    battery1, _ = ads7830.batteryPower()
    assert battery1 == 4.9
    assert ads7830.battery1Voltage == [100] * 24 + [200]

def test_voltage_battery2_second_time(ads7830):
    ads7830.readAdc = MagicMock(return_value=50)
    _, battery2 = ads7830.batteryPower()
    assert battery2 == 2.94
    assert ads7830.battery2Voltage == [150] * 24 + [50]

def test_voltage_other_channel(ads7830):
    ads7830.readAdc = MagicMock(return_value=200)
    voltage = ads7830.voltage(1)
    assert voltage == 0.78
    ads7830.readAdc.assert_called_once_with(1)
