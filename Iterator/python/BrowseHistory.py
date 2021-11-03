from StringIterator import StringIterator


class BrowseHistory:
    __urls = []

    def getUrls(self) -> list:
        return self.__urls

    def createIterator(self) -> StringIterator:
        return StringIterator(self)

    def push(self, url: str) -> None:
        self.__urls.append(url)

    def pop(self) -> str:
        return self.__urls.pop()
