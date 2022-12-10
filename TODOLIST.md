# # Bugs
 - [ ] data.csv가 UTF-8 일때는 입력이 잘 되는데 EUC-KR일때는 안됨(아예 못읽음) (2022.12.02)  
  
- - -
  
# # Features
 ## Core
 - [ ] 저장 기능
 - [ ] 검색(or 필터) 기능


 ## UI
 - [ ] GuiInterface 완성하기
 - [ ] PyQt5Interface 완성하기

 - [x] 불러오기 UI 추가
 - [ ] 불러오기 UI 수정(검색기능)
 
 - [ ] QInputDialog 부분도 추상화


 ## Code
 - Window의 내용물이 서로 너무 많이 연관되어 있어서 원하는 형태로의 분리가 어렵다.  
    Textbox 따로, Button 따로, Data 따로 클래스 분리해서 관리하고 싶은데, 이게 안된다.  
    하나로 합치기에는 Window클래스의 크기가 너무 커짐.  