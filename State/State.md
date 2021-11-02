Photoshop과 같은 Drawing Application을 만들고 있습니다.

툴타입을 변경했을 때 선택한 툴타입에 따라 기능이 달라지게 구현하고 싶습니다.

### Canvas 클래스

- method: void mouseDown()
- method: void mouseUp()

### ToolType

- Selection
- Brush
- Eraser

아래와 같이 구현을 하였습니다.

[dart 코드](dart/problem.dart)

[python 코드](python/problem.py)

### 문제

- 툴 타입의 개수가 늘어나거나
- 키보드 이벤트를 추가하는 등 기능 확장을 하려 할 때
- 구조를 유연하게 유지하기 쉽지 않다.

기능을 추가하더라도 유지보수가 수월한, 확장성이 있는 코드를 작성하고 싶습니다.
