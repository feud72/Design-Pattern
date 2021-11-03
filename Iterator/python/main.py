from BrowseHistory import BrowseHistory


def main():
    history = BrowseHistory()
    history.push("a")
    history.push("b")
    history.push("c")

    iterator = history.createIterator()

    while iterator.hasNext():
        print(iterator.current())
        iterator.next()


main()
