from abc import ABCMeta, abstractmethod


class Compressor(metaclass=ABCMeta):
    @abstractmethod
    def compress(self):
        pass
