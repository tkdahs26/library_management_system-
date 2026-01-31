# library_management_system-

프로젝트 개요

프로젝트는 Flask를 사용해 구현한 SQLite 기반의 도서관 관리 시스템입니다.<br>

면접 과제 이후 리팩토링을 통해 입력 처리와 구조를 개선했으며 <br>
사용자 로그인부터 도서 등록, 대여 및 재고 관리까지 기본적인 도서 관리 기능을 서버에서 처리하도록 구현했습니다
<br><br><br><br>
주요 기능
<br>
사용자 관리:<br>
 회원가입 및 로그인 기능<br>
 Flask session을 활용한 로그인 상태 관리<br><br>

도서 관리:<br>
 도서 등록<br>
 카테고리별 도서 조회<br><br>

 대여 시스템:<br>
 도서 대여<br>
 대여 시 재고 자동 관리<br>
 개인별 대여 이력 조회<br><br>


구현 특징<br>

 Flask를 사용한 REST API 방식의 서버 구성<br>
 SQLite를 활용한 데이터 저장<br>
 서버에서 사용자를 session에 저장 후 관리<br>
 도서 대여 시 재고 수량을 즉시 반영


서버 실행<br>
main.py<br>
기능 테스트<br>
test.py



개발 환경<br>

언어: Python<br>
프레임워크: Flask<br>
DB: SQLite<br>
Tool: PyCharm<br>

 

<img width="500" height="150" alt="library1" src="https://github.com/user-attachments/assets/694783b8-faf5-4b53-be15-3fa9be025a73" /> 
회원가입을 통해 사용자를 등록할 수 있으며 
로그인시 로그인한 사용자는 서버에서 세션을 통해 식별되며 페이지 이동 시에도 사용자 정보가 유지됩니다.
회원가입한 사용자 정보는 SQLite 데이터베이스에 저장됩니다.

<br><br><br><br><br><br>

<img width="500" height="350" alt="library1_1" src="https://github.com/user-attachments/assets/e543e830-cff0-4a29-8c7d-031f2756141b" /> 
회원가입한 사용자 정보는 SQLite 데이터베이스에 저장됩니다.
<br><br><br><br><br><br>



<img width="910" height="330" alt="library2" src="https://github.com/user-attachments/assets/e27947ab-1ff3-4db7-818d-b9a380595891" /> 
로그인 후 메인화면
<br>
로그인 후 메인 페이지에서
등록된 도서 목록을 테이블 형태로 확인할 수 있습니다.
<br><br><br><br><br><br>

<img width="1918" height="799" alt="library3" src="https://github.com/user-attachments/assets/188237aa-5f0e-4353-8e2c-c526f9f413a2" />


새 책을 등록할 수 있으며 이미 등록된 ISBN인 경우에는 새 레코드를 생성하지 않고 기존 도서의 재고 수량만 증가하도록 구현했습니다.







<br><br><br><br><br><br>
<img width="1918" height="799" alt="library3_1" src="https://github.com/user-attachments/assets/095bc954-2392-4a9c-acb2-4e38c75eb37d" />
책 등록하면 db에 등록됩니다  
<br><br><br><br><br><br>
<img width="1918" height="799" alt="library4" src="https://github.com/user-attachments/assets/636d3a4a-d6ad-4118-bf3c-111b19c16f0f" /> 

도서 제목의 일부만 입력해도 해당 도서를 검색할 수 있도록 구현했습니다.




<br><br><br><br><br>








<img width="1915" height="749" alt="library5" src="https://github.com/user-attachments/assets/18bc7da5-d114-4851-bb1d-17498ac180cf" />
검색 결과에서 도서를 선택해 대여하면 대여가 완료되며 해당 도서의 남은 재고 수량이 즉시 감소하는 것을 화면에서 확인할 수 있습니다.




<br><br><br><br><br><br>
<img width="1910" height="749" alt="library5_1" src="https://github.com/user-attachments/assets/e31458a5-d794-48c3-a433-bdbb0a045d9d" />
도서를 대여하면 대여 정보가 서버에 저장되며 대여한 도서와 대여 시점이 함께 저장.





<br><br><br><br><br><br>
<img width="1910" height="749" alt="library6" src="https://github.com/user-attachments/assets/c1d6a59a-20fc-4492-b929-defcaf886b54" />
사용자별 모든 대여 기록을 id값으로 분류해 내대여목록 클릭시 사용자는 자신이 대여한 도서 만을 확인 할 수 있습니다.












