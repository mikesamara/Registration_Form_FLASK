'''
Создать базу данных для хранения информации о книгах в библиотеке.
База данных должна содержать две таблицы: "Книги" и "Авторы".
В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.
В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
Необходимо создать связь между таблицами "Книги" и "Авторы".
Написать функцию-обработчик, которая будет выводить список всех книг с
указанием их авторов.
'''
from random import randint

from flask import Flask, render_template, jsonify
from models import db, Books, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app_1.db'
db.init_app(app)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-books')
def add_books():
    for _ in range(1, 4):
        author = Author(name=str(f' Author{_}'), last_name=str(f' Last_Name{_}'))
        db.session.add(author)
    db.session.commit()

    for i in range(1, 11):
        book = Books(name_books=f' Book{i}', year_publication=f' Year{randint(1975, 2012)}', count_books=randint(1, 10),
                     author_id=randint(1, 3))
        db.session.add(book)
    db.session.commit()


@app.route('/')
def index():
    books = Books.query.all()

    return render_template('index.html', books=books)


if __name__ == '__main__':
    app.run(debug=True)
