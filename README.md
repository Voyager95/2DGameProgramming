2DGameProgramming Term Project : Just Feel
======
![alt text](https://github.com/Voyager95/2DGameProgramming/blob/master/JustFeel_Main.png "Logo Title Text")
## 1. 게임 설명
- 제목: Just Feel
- 개요: 사용자가 자유롭게 음악에 맞추어서 노트를 기록하고 자신이 플레이할 수 있는 리듬 게임  
- 장르: 리듬 게임
- 주요 특징: 
  - 자신이 특정 음악에 맞게 노트를 기록하고 플레이 할 수 있음
  - 특정 키 입력이 아니라 패턴으로 입력을 함 
      > 노트에 맞추어 E키를 누른다. (X)  
      > 특정 시점에 맞추어 아무 키를 입력한다. (O)  
      > 특정 시간동안 어떤 위치에 있는 키를 연속으로 누른다. (O)  
    
## 2. Game State
Just Feel은 총 6개의 State로 구성되어있습니다.

#### -Title
 -	Roll: 플레이, 레코딩 스테이트로 이동 할 수 있는 화면입니다.
 -	Objects: 종료버튼, 플레이버튼, 레코딩버튼
 -	Input: 각 버튼 선택
 -	State Transition: 
    - 플레이버튼 -> SelectPlay
    - 레코딩버튼- > SelectRecord

#### -SelectPlay
  -	Roll: 플레이할 곡을 선택합니다.  
    *Music 폴더에 mp3파일과 jpr(레코딩)파일이 있는 경우에 표시 됩니다.
  -	Objects: 곡 리스트
  -	Input: 마우스를 통한 곡 버튼 선택
  -	State Transition:
    - ESC - > Title
    - 곡 선택 -> Play
    
#### -Play
![alt text](https://github.com/Voyager95/2DGameProgramming/blob/master/JustFeel_Play.png "Logo Title Text")
  -	Roll: 선택된 음악에 맞추어 노트가 생성되며 플레이어의 입력에 맞추어 노트에 맞는지 판단합니다.
  -	Objects: 배경이미지, 노트, 판정 효과
  - Input: 영문키, 숫자, 벡스페이스, 스페이스, 엔터
  - State Transition:
    - ESC -> SelectPlay
    - 곡완료 -> Score

#### - Score
  - Roll: Play State에서 낸 점수를 화면에 표시해 줍니다.
  - Objects: 점수 텍스트
  - Input: Enter
  - State Transition:
    -  Enter -> Title
    
#### -SelectRecord
  - Roll: 레코드할 곡을 선택합니다.
    *Music 폴더에 mp3파일들이 리스트로 됩니다.
  - Objects: 곡 리스트
  - Input: 마우스를 통한 곡 버튼 선택
  - State Transition:
    - ESC - > Title
    - 곡 선택 -> Record
    
#### -Record
![alt text](https://github.com/Voyager95/2DGameProgramming/blob/master/JustFeel_Record.png "Logo Title Text")
  - Roll: 선택된 음악이 재상되며 패턴을 입력하거나 키를 입력하면 해당 내용을 저장합니다.
  - Objects: 어떤것이 입력되고 있는지 화면에 표시 / 어떤 파일이름으로 저장할지 입력받는 창
  - Input: 영문키, 숫자, 벡스페이스, 스페이스, 엔터
  - State Transition:
    - ESC -> SelectRecord
    - 곡완료 -> Title

## 3. 필요한 기술
  - 수업시간에 배울 것으로 예상:
    - 음악 재생
  - 수업시간에 배우지 않을 것으로 예상:
    - 파일 입출력
    
## 4. 개발일정
1주차 - 키입력 모듈/ 리소스 준비

2주차 - 버튼, 노트, 배경 등의 요소(객체)

3주차 - Select record / Record

4주차 - Record / 파일 Json 저장

5주차 - Title / Select Play

6주차 - Play

7주차 - Play / Score

8주차 - 버그수정

## 사용된 음악

Alive by LiQWYD https://soundcloud.com/liqwyd
Creative Commons — Attribution 3.0 Unported — CC BY 3.0
Free Download / Stream: https://bit.ly/l_alive
Music promoted by Audio Library https://youtu.be/8xXFbq4J52E
