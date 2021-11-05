from abc import ABCMeta, abstractmethod


class UIControl(metaclass=ABCMeta):
    @abstractmethod
    def mouseDown(self) -> None:
        pass

    @abstractmethod
    def mouseUp(self) -> None:
        pass
