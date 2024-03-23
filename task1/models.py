from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

'''В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.'''
class Author(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    books_author = db.relationship('Books', backref=db.backref('author'), lazy=True)

    def __repr__(self):
        return f'Author {self.last_name} {self.name} '

'''В таблице "Книги" должны быть следующие поля: id, название, год издания,
количество экземпляров и id автора.'''
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_books = db.Column(db.String(80), nullable=True)
    year_publication = db.Column(db.String(80), nullable=True)
    count_books= db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id_'), nullable=True)

    def __repr__(self):
        return f'Book {self.name_books}, {self.year_publication}'
