import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from Servo import *

import pytest
from unittest.mock import MagicMock, patch
#from my_module import Servo, mapNum, servo_installation_position

# Mock the Adafruit_PCA9685 library to avoid calling actual hardware
adafruit_mock = MagicMock()
adafruit_mock.PCA9685.return_value = adafruit_mock
adafruit_mock.set_pwm_freq.return_value = None
adafruit_mock.set_pwm.return_value = None
with patch('Servo.Adafruit_PCA9685', adafruit_mock):

    @pytest.fixture
    def servo():
        return Servo()

    def test_mapNum():
        assert mapNum(50, 0, 100, 0, 10) == 5.0
        assert mapNum(25, 0, 100, 0, 10) == 2.5
        assert mapNum(75, 0, 100, 0, 10) == 7.5

    def test_Servo_init():
        servo = Servo()
        adafruit_mock.PCA9685.assert_called_with(0x40)
        adafruit_mock.set_pwm_freq.assert_called_with(50)
        assert adafruit_mock.set_pwm_freq.call_count == 2

    def test_Servo_setServoAngle(servo):
        servo.setServoAngle(0, 90)
        adafruit_mock.set_pwm.assert_called_with(0, 0, 2048)

        servo.setServoAngle(16, 90)
        adafruit_mock.set_pwm.assert_called_with(0, 0, 2048)

    def test_Servo_relax(servo):
        servo.relax()
        expected_calls = [((i+8, 4096, 4096),) * 3 for i in range(8)]
        assert adafruit_mock.set_pwm.call_args_list == expected_calls

    def test_servo_installation_position(servo):
        #servo = Servo()
        with patch('my_module.time.sleep') as mock_sleep:
            servo.servo_installation_position()
        expected_angles = [0 if i in (10, 13, 31) else 180 if i in (18, 21, 27) else 90 for i in range(32)]
        expected_calls = [((i, expected_angles[i]),) for i in range(32)]
        assert adafruit_mock.set_pwm.call_args_list == expected_calls
        assert mock_sleep.call_args == ((3,),)

