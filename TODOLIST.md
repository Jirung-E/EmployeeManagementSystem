# # Bugs
 - [ ] data.csv가 UTF-8 일때는 입력이 잘 되는데 EUC-KR일때는 안됨(아예 못읽음) (2022.12.02)  
  
- - -
  
# # Features
 ## Core
 - [ ] 저장 기능
 - [ ] 검색(or 필터) 기능


 ## UI
 - [x] 불러오기 UI 추가
 - [ ] 불러오기 UI 수정(검색기능)

 textbox들을 다 세부 클래스를 만들어서 관리할까?
 그렇게 하면 
```py
for e in textbox:  # textbox의 내용물은 전부 Textbox 클래스를 상속받음
    e.set()         # set은 Textbox의 virtual 함수
``` 
 같이 관리할수 있음
 (단, Textbox가 CSVData에 접근할수 있어야함)