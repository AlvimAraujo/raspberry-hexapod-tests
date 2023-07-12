import pytest
from unittest import mock
import time

import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from Buzzer import Buzzer

# Define a mock for RPi.GPIO
RPi_MOCK = mock.Mock()
RPi_MOCK.OUT = mock.Mock()
RPi_MOCK.setup = mock.Mock()
RPi_MOCK.output = mock.Mock()

# Replace RPi.GPIO with the mock
@mock.patch.dict('sys.modules', {'RPi': mock.Mock(), 'RPi.GPIO': RPi_MOCK})
def test_buzzer_on():
    # Create an instance of the Buzzer class
    buzzer = Buzzer()

    # Call the run method with '1' as input
    buzzer.run('1')

    # Check that the output pin was set to True
    RPi_MOCK.output.assert_called_once_with(buzzer.Buzzer_Pin, True)

    # Sleep for 3 seconds
    time.sleep(3)

    # Call the run method with '0' as input
    buzzer.run('0')

    # Check that the output pin was set to False
    RPi_MOCK.output.assert_called_with(buzzer.Buzzer_Pin, False)

@mock.patch.dict('sys.modules', {'RPi': mock.Mock(), 'RPi.GPIO': RPi_MOCK})
def test_buzzer_off():
    # Create an instance of the Buzzer class
    buzzer = Buzzer()

    # Call the run method with '0' as input
    buzzer.run('0')

    # Check that the output pin was set to False
    RPi_MOCK.output.assert_called_once_with(buzzer.Buzzer_Pin, False)

@mock.patch.dict('sys.modules', {'RPi': mock.Mock(), 'RPi.GPIO': RPi_MOCK})
def test_buzzer_toggle():
    # Create an instance of the Buzzer class
    buzzer = Buzzer()

    # Call the run method with '1' as input
    buzzer.run('1')

    # Check that the output pin was set to True
    RPi_MOCK.output.assert_called_once_with(buzzer.Buzzer_Pin, True)

    # Call the run method with '0' as input
    buzzer.run('0')

    # Check that the output pin was set to False
    RPi_MOCK.output.assert_called_with(buzzer.Buzzer_Pin, False)

    # Call the run method with '1' as input
    buzzer.run('1')

    # Check that the output pin was set to True again
    RPi_MOCK.output.assert_called_with(buzzer.Buzzer_Pin, True)

