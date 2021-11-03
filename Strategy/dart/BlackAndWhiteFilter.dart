import 'Filter.dart';

class BlackAndWhiteFilter implements Filter {
  @override
  void apply(String fileName) {
    print("$fileName: Applying B&W filter");
  }
}
