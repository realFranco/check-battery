from abc import ABC, abstractmethod


class CheckBattery(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def getBatteryPercentage() -> float:
        pass
