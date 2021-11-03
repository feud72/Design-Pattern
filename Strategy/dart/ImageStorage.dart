import 'Compressor.dart';
import 'Filter.dart';

class ImageStorage {
  void store(String fileName, Compressor compressor, Filter filter) {
    compressor.compress(fileName);
    filter.apply(fileName);
  }
}
