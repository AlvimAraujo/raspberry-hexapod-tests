import time
import RPi.GPIO as GPIO
import pytest

class TestBuzzer:
    @pytest.fixture(autouse=True)
    def buzzer(self):
        b = Buzzer()
        yield b
        b.run('0')

    def test_buzzer_on(self, buzzer):
        buzzer.run('1')
        time.sleep(1)
        assert GPIO.input(buzzer.Buzzer_Pin) == GPIO.HIGH

    def test_buzzer_off(self, buzzer):
        buzzer.run('0')
        time.sleep(1)
        assert GPIO.input(buzzer.Buzzer_Pin) == GPIO.LOW
