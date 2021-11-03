import 'BrowseHistory.dart';

void main(List<String> args) {
  var history = new BrowseHistory();
  history.push("a");
  history.push("b");
  history.push("c");

  var iterator = history.createIterator();

  while (iterator.hasNext()) {
    var url = iterator.current();
    print(url);
    iterator.next();
  }
}
