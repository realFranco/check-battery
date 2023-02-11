from abc import ABC, abstractmethod


class Notification(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def exposeNotification() -> bool:
        pass
