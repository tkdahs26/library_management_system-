# library_management_system-

Flask와 파이참 인터페이스를 활용한 SQLite를 기반으로 한 RESTful API 도서관 관리 시스템입니다.
사용자 인증, 도서 등록 및 조회, 도서 재고 관리, 대여 이력 조회,관리 기능을 포함하고 있습니다.


Python (Flask)
DB: SQLite
Tool: PyCharm


주요기능
라우팅방식으로 통신했고
1.사용자관리: 회원가입 및 로그인 (flask.session을 활용)<br>
2. 도서관리: 도서 등록 및 카테고리별 조건 검색<br>
3. 대여시스템: 실시간 대여 처리 및 재고 관리, 개인 대여 목록 조회<br>


서버 실행<br>
main.py


기능 테스트<br>
test.py



<img width="500" height="150" alt="library1" src="https://github.com/user-attachments/assets/694783b8-faf5-4b53-be15-3fa9be025a73" /> 로그인화면 로그인 성공 시 app.secret_key를 활용해 user_id를 생성하여 페이지 이동 시에도 사용자의 user_id가 유지됩니다.      

<img width="500" height="350" alt="library1_1" src="https://github.com/user-attachments/assets/e543e830-cff0-4a29-8c7d-031f2756141b" /> 회원가입 후 db에 정보가 저장됨

<img width="910" height="330" alt="library2" src="https://github.com/user-attachments/assets/e27947ab-1ff3-4db7-818d-b9a380595891" /> 로그인 후 메인화면 render_template을 통해 HTML로 전달 후 html에서 테이블 형식으로 출력   <br><br>

<img width="1918" height="799" alt="library3" src="https://github.com/user-attachments/assets/188237aa-5f0e-4353-8e2c-c526f9f413a2" />새책등록했을때 
ISBN이 중복될 경우, 신규 행이 만들어지지않고 남은권수가 등록수량만큼 증가함 

<img width="1918" height="799" alt="library3_1" src="https://github.com/user-attachments/assets/095bc954-2392-4a9c-acb2-4e38c75eb37d" /><br><br>책 db화면 books테이블

<img width="1918" height="799" alt="library4" src="https://github.com/user-attachments/assets/636d3a4a-d6ad-4118-bf3c-111b19c16f0f" /><br><br> 책 검색 실행 contains함수를 사용해서 harry potter 를 검색했을때 potter만 검색해도 검색결과가 뜨고 
JavaScript를 통해 사용자에게 알림

<img width="1915" height="749" alt="library5" src="https://github.com/user-attachments/assets/18bc7da5-d114-4851-bb1d-17498ac180cf" /><br><br>책 대여하기에 성공하면 total_copies값을 -1해서 db에 넘김 남은권수가 하나 줄어듬

<img width="1910" height="749" alt="library5_1" src="https://github.com/user-attachments/assets/e31458a5-d794-48c3-a433-bdbb0a045d9d" /><br><br>대여했을때 유저의 user_id 값과 빌린 book_id 값을 db에 저장
<img width="1910" height="749" alt="library6" src="https://github.com/user-attachments/assets/c1d6a59a-20fc-4492-b929-defcaf886b54" /><br><br>
load 테이블에서 사용자와 user_id가 일치하는 칼럼을 조회하면 내가 대여한책 조회 함 













