import 'Iterator.dart';
import 'StringIterator.dart';

class BrowseHistory {
  List<String> _urls = [];

  List<String> get urls => _urls;

  Iterator createIterator() {
    return new StringIterator(history: this);
  }

  void push(String url) {
    urls.add(url);
  }

  String pop() {
    return urls.removeLast();
  }
}
