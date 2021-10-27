class EditorState:
    __content = str()

    def __init__(self, content: str) -> None:
        self.__content = content

    def getContent(self) -> str:
        return self.__content
