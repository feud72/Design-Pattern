class BrowseHistory:
    __urls = []

    def getUrls(self) -> list:
        return self.__urls

    def push(self, url: str) -> None:
        self.__urls.append(url)

    def pop(self) -> str:
        return self.__urls.pop()


def main():
    history = BrowseHistory()
    history.push("a")
    history.push("b")
    history.push("c")

    for url in history.getUrls():
        print(url)


main()
