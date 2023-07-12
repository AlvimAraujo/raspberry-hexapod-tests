import pytest
import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from Kalman import *

@pytest.fixture
def kalman():
    return Kalman_filter(0.01, 0.1)

def test_kalman_output(kalman):
    assert kalman.kalman(10) == 10

def test_kalman_variance(kalman):
    for i in range(10):
        kalman.kalman(10)
    assert kalman.P_k1_k1 == pytest.approx(1.01, 0.01)

def test_kalman_gain(kalman):
    for i in range(10):
        kalman.kalman(10)
    assert kalman.Kg == pytest.approx(0.499, 0.01)

def test_kalman_state(kalman):
    kalman.kalman(10)
    assert kalman.x_k_k1 == 10

def test_kalman_adc_old(kalman):
    kalman.kalman(10)
    assert kalman.kalman_adc_old == 10

def test_kalman_output_with_noise(kalman):
    assert kalman.kalman(10) == 10
    assert kalman.kalman(100) == pytest.approx(26.6, 0.1)

