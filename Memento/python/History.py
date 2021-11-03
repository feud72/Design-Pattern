from editor_state import EditorState


class History:
    __states = list()

    def push(self, state: EditorState):
        self.__states.append(state)

    def pop(self):
        return self.__states.pop()
