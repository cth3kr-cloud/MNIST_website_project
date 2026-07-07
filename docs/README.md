interface_spec 에서는 각 세부 프로젝트에서 사용할 공용 변수나 함수의 사용처를 명세하는 역활을 하는 md 파일입니다.
interface_spec 는 다음과 같은 방법으로 작성해 주십시오




project_log 에서는 보다 구체적으로 프로젝트 진행 현왕을 작성하는 md 파일입니다.
project_log 는 다음과 같은 방법으로 작성해 주십시오



# 1. commit

  ## YYYY-MM-DD
  ### Commit
  
  - 브랜치: 어떤 브랜치에 commit 했는지
  - 메시지: 커밋 메시지 내용
  - 변경 사항: 어떤 파일/코드가 수정되었는지
  - 의사결정: 왜 이 커밋을 만들었는지, 선택한 이유 또는 설명
  - 배운 점: 작업 중 새로 알게 된 점
  - 비고: 그 밖에 쓸 점(공지사항 등)

  ex)
  ## 2026-07-07
  ### Commit
  
  - 브랜치: main
  - 메시지: Add .gitignore file for Python and Node.js projects
  - 변경 사항: .gitignore 파일을 docs에 추가함.
  - 의사결정: 필요없는 파일을 프로젝트에서 숨기기 위해 추가함.
  - 배운 점: pycharm에서 내장으로 생성하는 .gitignore와 직접 생성한 .gitignore의 역활이 다르다는 것을 배움
  - 비고: 다음 작업은 .gitignore 작성 예정.



# 2. push

 - ## YYYY-MM-DD
 - ### push
 - 브랜치: 어떤 브랜치에 push 챘는지
 - 히스토리: push할 부분이 이전에 commit된 기록(메시지) 작성
 - 비고: 그 밖에 쓸 점(공지사항 등)
 - 
 ex)
 - ## 2026-07-11
 - ### push
 - 브랜치: main
 - 히스토리:
   - {Add .gitignore file for Python and Node.js projects, 2026-07-07}
 - 비고:



# 3. 동아리 활동

  - ## YYYY-MM-DD
  - ### 동아리 활동
  - 주제: 활동 주제가 무엇이었는지 
  - 결론: 각 팀원이 할 점 
  - 협업 관련: 팀원에게 공유한 내용이나 Pull Request 생성 여부
  - 
  ex)
  - ## YYYY-MM-DD
  - ### 동아리 활동
  - 주제: 주제 선정 및 역활 분담 
  - 결론: 
    -동아리 주제는 "MNIST 웹사이트 만들기"로 결정
    - 프론트 엔드(), 벡엔드(), 데이터 엔지니어링(), AI()로 역활분
  - 협업 관련: 
