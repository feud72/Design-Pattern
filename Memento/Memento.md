# Memento 패턴

워드프로세서를 만들고 있습니다.

Editor 클래스는 현재 작성 중인 문자열을 저장합니다.

이 클래스에 Save, Undo 기능을 구현하려 합니다.

### Editor 클래스

- field : content (String)

- method : createState (현재 상태를 저장)

- method : restore (이전 상태로 되돌리기)
