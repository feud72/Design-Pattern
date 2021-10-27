from Editor import Editor
from History import History

editor = Editor()
history = History()

editor.setContent("a")
history.push(editor.createState())
editor.setContent("b")
history.push(editor.createState())
editor.setContent("c")

print(editor.getContent())
editor.restore(history.pop())
print(editor.getContent())
editor.restore(history.pop())
print(editor.getContent())
