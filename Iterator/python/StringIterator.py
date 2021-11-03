from CustomIterator import Iterator


class StringIterator(Iterator):
    def __init__(self, history) -> None:
        self.__history = history
        self.__index = 0

    def hasNext(self) -> bool:
        return len(self.__history.getUrls()) > self.__index

    def next(self) -> None:
        self.__index += 1

    def current(self) -> str:
        return self.__history.getUrls()[self.__index]
