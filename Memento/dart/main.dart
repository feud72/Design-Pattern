import 'Editor.dart';
import 'History.dart';

void main(List<String> args) {
  var editor = new Editor();
  var history = new History();

  editor.content = "a";
  history.push(editor.createState());
  editor.content = "b";
  history.push(editor.createState());
  editor.content = "c";

  print(editor.content);
  editor.restore(history.pop());
  print(editor.content);
  editor.restore(history.pop());
  print(editor.content);
}
