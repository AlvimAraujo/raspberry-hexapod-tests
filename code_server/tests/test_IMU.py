import sys
import os
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from IMU import IMU

import pytest
from unittest.mock import MagicMock, patch
#from imu import IMU

class TestIMU:

    @pytest.fixture
    def imu(self):
        return IMU()

    @patch.object(IMU, 'average_filter', return_value=(0, 0))
    def test_imuUpdate(self, mock_avg_filter, imu):
        imu.imuUpdate()
        assert imu.q0 == 1
        assert imu.q1 == 0
        assert imu.q2 == 0
        assert imu.q3 == 0
        assert imu.pitch == 0
        assert imu.roll == 0
        assert imu.yaw == 0

    def test_average_filter(self, imu):
        imu.sensor = MagicMock()
        imu.sensor.get_accel_data.return_value = {'x': 1, 'y': 2, 'z': 3}
        imu.sensor.get_gyro_data.return_value = {'x': 4, 'y': 5, 'z': 6}

        accel_data, gyro_data = imu.average_filter()
        assert accel_data == {'x': 1.0, 'y': 2.0, 'z': -6.78}
        assert gyro_data == {'x': 4.0, 'y': 5.0, 'z': 6.0}
