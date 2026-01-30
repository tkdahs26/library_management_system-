import os
import secrets
from flask import session
import redirect
import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect, render_template
app = Flask(__name__)
app.secret_key =os.urandom(24).hex()
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'library.db')

db = SQLAlchemy(app)


@app.route('/')
def index():    # 기본 홈페이지
    return render_template('login.html')

@app.route('/books', methods=['GET'])
def books_form():
    return render_template('books.html')

@app.route('/auth/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    full_name = db.Column(db.String(120))
    """
        def __init__(self,id,username,password,email,full_name):
            self.id = id
            self.username = username
            self.password = password
            self.email = email
            self.full_name = full_name
    """

@app.route('/auth/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    full_name = request.form.get('full_name')


    #생성자 호출
    new_user = User(username=username,
        password=password,
        email=email,
        full_name=full_name
    )
    db.session.add(new_user)
    db.session.commit()
    return """
        <script>
            alert('회원가입이 성공했습니다');
            location.href = '/';
        </script>
    """


@app.route('/auth/login', methods=['POST'])
def login():

    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        session['user_id'] = user.id # 로그인 정보 세션에 저장
        return redirect('/home')

    return """
        <script>
            alert('로그인 실패');
            location.href = '/';
        </script>
    """


@app.route('/home')
def home():
    all_books = Book.query.all()    # DB의 모든 데이터를 가져옴

    return render_template('home.html', books=all_books)    # templates/home.html 파일을 열면서 데이터를 전달함


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(20))
    category = db.Column(db.String(50))
    total_copies = db.Column(db.Integer, default=1)

@app.route('/books/add', methods=['POST'])
def add_book():
    isbn = request.form.get('isbn')

    exist_book = Book.query.filter_by(isbn=isbn).first()
    if exist_book:
        add_count = int(request.form.get('total_copies', 1))
        exist_book.total_copies += add_count

        db.session.commit()
        return f"""
                <script>
                    alert('추가되었습니다.');
                    location.href = '/home';
                </script>
            """


    else:
       title = request.form.get('title')
       author = request.form.get('author')
       isbn = request.form.get('isbn')
       category = request.form.get('category')
       total_copies = int(request.form.get('total_copies', 1))

       new_book = Book(
          title=title,
          author=author,
          isbn=isbn,
          category=category,
          total_copies=int(total_copies)
          )
       db.session.add(new_book)
       db.session.commit()
       return redirect('/home')





@app.route('/home/search', methods=['GET'])
def search_books():


    search_title = request.args.get('title')
    book_exists = Book.query.filter(Book.title.contains(search_title)).first()

    if book_exists:

        print(f"'{search_title}' 책이 있습니다.")
        return f"""
                <script>
                    alert('{search_title} 책이 있습니다');
                    location.href = '/home';
                </script>
            """
    else:
        print(f"'{search_title}' 책이 없습니다. ---")
        return f"""
                <script>
                    alert('{search_title} 책이 없습니다.');
                    history.back();
                </script>
            """



class Loan(db.Model):
    __tablename__ = 'loans'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    loan_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    is_returned = db.Column(db.Boolean, default=False)
    book = db.relationship('Book', backref='loans') #첫번째매개변수 참조하는 클래스명
@app.route('/loans', methods=['POST'])
def add_loan():

    current_user_id = session.get('user_id')
    selected_id = request.form.getlist('borrow_id')
    if not selected_id:
        return "<script>alert('선택된 책이 없습니다.'); history.back();</script>"
    for book_id in selected_id:
        book = Book.query.get(int(book_id))  # ID로 책 찾기

        if book:
            if book.total_copies > 0:
                book.total_copies -= 1
                new_loan = Loan(user_id=current_user_id, book_id=book.id)
                db.session.add(new_loan)
            else:

                print(f"ID {book_id}번 책은 재고가 없습니다.")


    db.session.commit()

    return """
            <script>
                alert('선택하신 도서의 대여가 완료되었습니다!');
                location.href = '/home';
            </script>
        """



@app.route('/users/me/loans', methods=['GET'])
def get_my_loans():
    user_id = session.get('user_id')

    if not user_id:
        return "<script>alert('로그인이 필요합니다.'); location.href='/login';</script>"


    my_loans = Loan.query.filter_by(user_id=user_id).all()

    return render_template('my_loans.html', loans=my_loans)















if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)











