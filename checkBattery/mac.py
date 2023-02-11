"""
Inherited from Notification and 
"""
import os
import re

from config import BATTERY_LEVEL
from content.checkBattery import CheckBattery
from content.notification import Notification


class Mac(CheckBattery, Notification):

    def __init__(self):
        pass

    def getBatteryPercentage(self):
        # @todo: Write the command as a constant, in order to be fully customized.
        batteryPercentageTarget: str = re.findall(
            pattern=r'([0-9]{2})%', 
            string=os.popen('pmset -g batt').read()
        )
        if [] == batteryPercentageTarget:
            print('No data collected.')
            return -1

        return float(batteryPercentageTarget[0])

    def exposeNotification(self) -> bool:
        batteryLevel: float = self.getBatteryPercentage()
        if batteryLevel < 0:
            print('No notification about the battery level was send it.')
            return False

        if batteryLevel > BATTERY_LEVEL:
            print(f'The battery level it is ok to send notification ({batteryLevel}%).')
            return False

        notificationTitle: str = 'Battery Health: Charge is recommend.'
        notificationContent: str = f'The battery level is reaching 25% of charge ({batteryLevel}%), please charge ' + \
                                   'your MacBook.'

        # @todo: Write the command as a constant, in order to be fully customized.
        os.popen(f'osascript -e \'display notification "{notificationContent}" with title "{notificationTitle}"\'')

        return True
