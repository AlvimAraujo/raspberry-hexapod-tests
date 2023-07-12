import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

#sys.path.append('/home/arau/code_server/')

from ADS7830 import *

def test_readAdc():
    adc = ADS7830()
    assert adc.readAdc(0) >= 0 and adc.readAdc(0) <= 255
    assert adc.readAdc(1) >= 0 and adc.readAdc(1) <= 255
    assert adc.readAdc(2) >= 0 and adc.readAdc(2) <= 255
    assert adc.readAdc(3) >= 0 and adc.readAdc(3) <= 255
    assert adc.readAdc(4) >= 0 and adc.readAdc(4) <= 255
    assert adc.readAdc(5) >= 0 and adc.readAdc(5) <= 255
    assert adc.readAdc(6) >= 0 and adc.readAdc(6) <= 255
    assert adc.readAdc(7) >= 0 and adc.readAdc(7) <= 255

def test_voltage():
    adc = ADS7830()
    assert adc.voltage(0) == round((adc.readAdc(0)/255.0)*5.0, 2)
    assert adc.voltage(1) == round((adc.readAdc(1)/255.0)*5.0, 2)
    assert adc.voltage(2) == round((adc.readAdc(2)/255.0)*5.0, 2)
    assert adc.voltage(3) == round((adc.readAdc(3)/255.0)*5.0, 2)
    assert adc.voltage(4) == round((adc.readAdc(4)/255.0)*5.0, 2)
    assert adc.voltage(5) == round((adc.readAdc(5)/255.0)*5.0, 2)
    assert adc.voltage(6) == round((adc.readAdc(6)/255.0)*5.0, 2)
    assert adc.voltage(7) == round((adc.readAdc(7)/255.0)*5.0, 2)

def test_batteryPower():
    adc = ADS7830()
    assert adc.batteryPower() == (round(adc.voltage(0)*3,2), round(adc.voltage(4)*3,2))

