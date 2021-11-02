import 'Canvas.dart';
import 'BrushTool.dart';
import 'EraserTool.dart';

void main(List<String> args) {
  var canvas = new Canvas(currentTool: new BrushTool());

  canvas.mouseDown();
  canvas.mouseUp();

  canvas.currentTool = new EraserTool();
  canvas.mouseDown();
  canvas.mouseUp();
}
