from EditorState import EditorState


class Editor:
    __content = str()

    def createState(self) -> EditorState:
        return EditorState(self.__content)

    def restore(self, state: EditorState) -> None:
        self.__content = state.getContent()

    def getContent(self):
        return self.__content

    def setContent(self, content: str):
        self.__content = content
