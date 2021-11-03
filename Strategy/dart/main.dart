import 'BlackAndWhiteFilter.dart';
import 'HighContrastFilter.dart';
import 'ImageStorage.dart';
import 'JPEGCompressor.dart';
import 'PngCompressor.dart';

void main(List<String> args) {
  var image = ImageStorage();
  image.store("image1", new JpegCompressor(), new BlackAndWhiteFilter());
  image.store("image2", new PngCompressor(), new HighContrastFilter());
}
