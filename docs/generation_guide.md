# 📖 Project Documents Guide

프로젝트에서 사용하는 문서들의 역할과 작성 규칙을 설명합니다.

---

# 📌 Commit Convention

모든 Commit은 아래 형식을 따라 작성합니다.

```text
<type>(<part>): <description>
```

예시

```text
feat(ai): DenseLayer 구현
fix(backend): 이미지 업로드 오류 수정
docs(main): README 수정
```

## Commit Type

| 타입 | 의미 | 예시 |
|------|------|------|
| **feat** | 새로운 기능 추가 | `feat(ai): 역전파 알고리즘 구현` |
| **fix** | 버그 수정 | `fix(ai): Softmax 계산 오류 수정` |
| **docs** | 문서 수정 | `docs(data): README 업데이트` |
| **refactor** | 기능 변화 없는 코드 개선 | `refactor(front-end): Network 클래스 분리` |
| **style** | 코드 스타일 변경 (공백, 들여쓰기 등) | `style(backend): 코드 포맷 정리` |
| **test** | 테스트 코드 작성 | `test(ai): DenseLayer 단위 테스트 추가` |
| **chore** | 설정 파일 및 기타 작업 | `chore(main): .gitignore 수정` |

---

# 📌 Interface Specification

`interface_spec.md`는 프로젝트의 각 세부 파트에서 공통으로 사용하는 **변수, 함수, 클래스, API** 등을 정의하는 문서입니다.

예를 들어,

- AI ↔ Backend
- Backend ↔ Frontend

간의 인터페이스를 명세합니다.

> **인터페이스가 변경될 경우 반드시 해당 문서를 먼저 수정한 후 개발을 진행합니다.**

---

# 📌 Project Log

`project_log.md`는 프로젝트 진행 상황을 기록하는 문서입니다.

기록은 크게 **Commit**, **Push**, **동아리 활동**으로 나누어 작성합니다.

---

## 1️⃣ Commit

### 작성 양식

```md
## YYYY-MM-DD

### Commit

- 브랜치:
- 메시지:
- 변경 사항:
- 의사결정:
- 배운 점:
- 비고:
```

### 예시

```md
## 2026-07-07

### Commit

- 브랜치: main
- 메시지: chore(main): Add .gitignore file
- 변경 사항:
  - .gitignore 생성
- 의사결정:
  - 불필요한 파일이 Git에 올라가지 않도록 설정
- 배운 점:
  - PyCharm의 .idea/.gitignore와 프로젝트 루트의 .gitignore는 역할이 다르다.
- 비고:
  - 다음 작업은 requirements.txt 작성
```

---

## 2️⃣ Push

### 작성 양식

```md
## YYYY-MM-DD

### Push

- 브랜치:
- 포함된 Commit:
- 비고:
```

### 예시

```md
## 2026-07-11

### Push

- 브랜치: main

- 포함된 Commit:
  - chore(main): Add .gitignore file (2026-07-07)
  - docs(main): Add README (2026-07-08)

- 비고:
  - GitHub 원격 저장소와 동기화 완료
```

---

## 3️⃣ 동아리 활동

### 작성 양식

```md
## YYYY-MM-DD

### 동아리 활동

- 주제:
- 결론:
- 협업 관련:
```

### 예시

```md
## 2026-07-12

### 동아리 활동

- 주제:
  - 프로젝트 주제 선정 및 역할 분담

- 결론:
  - 프로젝트 주제:
    - GitHub를 활용한 실무형 협업 환경에서의 손글씨 인식 AI 웹 시스템 개발
  - 역할 분담:
    - Front-end : 홍길동
    - Back-end : 김철수
    - Data Engineering : 이영희
    - AI : 조태현

- 협업 관련:
  - Interface Specification 작성 완료
  - GitHub 저장소 생성
```

---

# 📌 작성 규칙

- Commit 후에는 **Commit 로그를 작성**합니다.
- Push 후에는 **Push 로그를 작성**합니다.
- 동아리 활동이 있는 날에는 **회의 내용과 역할 분담을 기록**합니다.
- 중요한 설계 변경 사항은 반드시 `interface_spec.md`에도 반영합니다.
