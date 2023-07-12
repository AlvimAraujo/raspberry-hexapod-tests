import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from Led import *

import pytest
from unittest.mock import MagicMock
from rpi_ws281x import Color

#from led import Led

def test_led_init():
    led = Led()
    assert led.strip.numPixels() == 7

def test_led_typr():
    led = Led()
    assert led.LED_TYPR('GRB', 0x00FF00) == Color(0xFF, 0x00, 0x00)
    assert led.LED_TYPR('RGB', 0x00FF00) == Color(0x00, 0xFF, 0x00)
    assert led.LED_TYPR('BGR', 0x00FF00) == Color(0x00, 0x00, 0xFF)
    assert led.LED_TYPR('GBR', 0x00FF00) == Color(0xFF, 0x00, 0x00)
    assert led.LED_TYPR('RBG', 0x00FF00) == Color(0x00, 0x00, 0xFF)
    assert led.LED_TYPR('BRG', 0x00FF00) == Color(0x00, 0xFF, 0x00)

def test_color_wipe():
    led = Led()
    led.strip.setPixelColor = MagicMock()
    led.strip.show = MagicMock()
    led.colorWipe(led.strip, 0x00FF00)
    assert led.strip.setPixelColor.call_count == 7
    assert led.strip.show.call_count == 7

def test_theater_chase():
    led = Led()
    led.strip.setPixelColor = MagicMock()
    led.strip.show = MagicMock()
    led.theaterChase(led.strip, 0x00FF00)
    assert led.strip.setPixelColor.call_count == 7
    assert led.strip.show.call_count == 70

def test_wheel():
    led = Led()
    assert led.wheel(0) == Color(255, 0, 0)
    assert led.wheel(85) == Color(0, 255, 0)
    assert led.wheel(170) == Color(0, 0, 255)
    assert led.wheel(255) == Color(255, 0, 0)

def test_rainbow():
    led = Led()
    led.strip.setPixelColor = MagicMock()
    led.strip.show = MagicMock()
    led.rainbow(led.strip)
    assert led.strip.setPixelColor.call_count == 7
    assert led.strip.show.call_count == 256

def test_rainbow_cycle():
    led = Led()
    led.strip.setPixelColor = MagicMock()
    led.strip.show = MagicMock()
    led.rainbowCycle(led.strip)
    assert led.strip.setPixelColor.call_count == 7
    assert led.strip.show.call_count == 1280

def test_led_index():
    led = Led()
    led.strip.setPixelColor = MagicMock()
    led.strip.show = MagicMock()
    led.ledIndex(0b00000101, 0xFF, 0x00, 0x00)
    assert led.strip.setPixelColor.call_count == 2
    assert led.strip.show.call_count == 1

def test_light():
    led = Led()
    led.strip.setPixelColor = MagicMock()
    led.strip.show = MagicMock()
    led.light([0xFF, 0x00, 0x00])
    assert led.strip.setPixelColor.call_count == 0
    assert led.strip.show.call_count == 0
