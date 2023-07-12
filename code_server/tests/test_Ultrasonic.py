import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from Ultrasonic import Ultrasonic

import time
from unittest.mock import patch, MagicMock
import pytest

#from ultrasonic import Ultrasonic

class TestUltrasonic:
    def test_init(self):
        with patch.object(GPIO, 'setwarnings') as mock_setwarnings, \
             patch.object(GPIO, 'setmode') as mock_setmode, \
             patch.object(GPIO, 'setup') as mock_setup:
            ultrasonic = Ultrasonic()
            assert ultrasonic.trigger_pin == 27
            assert ultrasonic.echo_pin == 22
            mock_setwarnings.assert_called_once_with(False)
            mock_setmode.assert_called_once_with(GPIO.BCM)
            mock_setup.assert_has_calls([call(27, GPIO.OUT), call(22, GPIO.IN)])

    def test_send_trigger_pulse(self):
        with patch.object(GPIO, 'output') as mock_output:
            ultrasonic = Ultrasonic()
            ultrasonic.send_trigger_pulse()
            mock_output.assert_has_calls([call(27, True), call(27, False)])
            mock_output.assert_called_once()

    def test_wait_for_echo_when_input_is_value(self):
        with patch.object(GPIO, 'input', return_value=True) as mock_input:
            ultrasonic = Ultrasonic()
            ultrasonic.wait_for_echo(True, 10000)
            mock_input.assert_called_once_with(22)

    def test_wait_for_echo_when_input_is_not_value_and_timeout_not_expired(self):
        with patch.object(GPIO, 'input', side_effect=[False, False, True]) as mock_input:
            ultrasonic = Ultrasonic()
            ultrasonic.wait_for_echo(True, 10000)
            mock_input.assert_has_calls([call(22), call(22), call(22)])
            assert mock_input.call_count == 3

    def test_wait_for_echo_when_input_is_not_value_and_timeout_expired(self):
        with patch.object(GPIO, 'input', return_value=False) as mock_input:
            ultrasonic = Ultrasonic()
            with pytest.raises(TimeoutError):
                ultrasonic.wait_for_echo(True, 1)
            mock_input.assert_has_calls([call(22), call(22), call(22), call(22)])

    def test_getDistance(self):
        with patch.object(Ultrasonic, 'send_trigger_pulse'), \
             patch.object(Ultrasonic, 'wait_for_echo', side_effect=[[True, True, False], [True, False, False], [True, False, True]]), \
             patch('time.time', side_effect=[0, 1, 2, 3, 4, 5, 6, 7]):
            ultrasonic = Ultrasonic()
            assert ultrasonic.getDistance() == 86
