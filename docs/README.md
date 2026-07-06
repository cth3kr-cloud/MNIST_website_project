interface_spec 에서는 각 세부 프로젝트에서 사용할 공용 변수나 함수의 사용처를 명세하는 역활을 하는 md 파일입니다.
interface_spec 는 다음과 같은 방법으로 작성해 주십시오




project_log 에서는 보다 구체적으로 프로젝트 진행 현왕을 작성하는 md 파일입니다.
project_log 는 다음과 같은 방법으로 작성해 주십시오



1. commit
  ## YYYY-MM-DD
  ### Commit
  - 메시지: 커밋 메시지 내용
  - 변경 사항: 어떤 파일/코드가 수정되었는지
  - 의사결정: 왜 이 커밋을 만들었는지, 선택한 이유 또는 설명
  - 배운 점: 작업 중 새로 알게 된 점
  - 비고: 그 밖에 쓸 점(공지사항 등)

  ex)
  ## 2026-07-06
  ### Commit
  - 메시지: Add image upload API
  - 변경 사항: `predict.py`에서 모델 역전파에 대한 7~15 줄 코드 추가
  - 의사결정: softmax + cross entropy 미분값을 통해 출력층과 은닉층 사이의 역전파를 구현
  - 배운 점: softmax + cross entropy 의 미분값은 (이상치 y) - y 임
  - 비고: protest_method 공용 변수의 이름을 pm으로 변경함 이점 유의 바



2. push
 - ## YYYY-MM-DD
 - ### push
 - 브랜치: 어떤 브랜치에 push 챘는지
 - 히스토리: push할 부분이 이전에 commit된 기록 작성
 - 비고: 그 밖에 쓸 점(공지사항 등)
 - 
 ex)
 - ## 2026-07-11
 - ### push
 - 브랜치: eature/ai
 - 히스토리: 2026-06-31, 2026-07-09, 2026-07-11
 - PUll request 여부: 했으면 어떤 branch를 merge 했는지
 - 비고:



3. 동아리 활동
  - ## YYYY-MM-DD
  - ### 동아리 활동
  - 주제: 활동 주제가 무엇이었는지 
  - 결론: 각 팀원이 할 점 
  - 협업 관련: 팀원에게 공유한 내용이나 Pull Request 생성 여부
  - 
  ex)
  - ## YYYY-MM-DD
  - ### 동아리 활동
  - 주제: 활동 주제가 무엇이었는지 
  - 결론: 각 팀원이 할 점 
  - 협업 관련: 팀원에게 공유한 내용이나 Pull Request 생성 여부
