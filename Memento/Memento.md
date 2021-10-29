## Memento 패턴

문자열을 저장하는 Editor 클래스가 있다.

Editor 클래스에 Undo 기능을 구현하려 한다.

### Editor 클래스

- field : content (String)
- method : createState (현재 상태를 저장)
- method : restore (이전 상태로 되돌리기)
