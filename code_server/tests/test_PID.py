import pytest
import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from PID import *

def test_pid_compute():
    pid = Incremental_PID(P=1.0, I=0.5, D=0.2)
    pid.setPoint = 10.0
    feedback_val = 8.0
    output = pid.PID_compute(feedback_val)
    assert output == pytest.approx(3.0, rel=1e-2)

def test_set_Kp():
    pid = Incremental_PID()
    pid.setKp(1.0)
    assert pid.Kp == 1.0

def test_set_Ki():
    pid = Incremental_PID()
    pid.setKi(0.5)
    assert pid.Ki == 0.5

def test_set_Kd():
    pid = Incremental_PID()
    pid.setKd(0.2)
    assert pid.Kd == 0.2

def test_set_I_saturation():
    pid = Incremental_PID()
    pid.setI_saturation(5.0)
    assert pid.I_saturation == 5.0
