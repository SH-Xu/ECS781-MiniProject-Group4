import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Book(db.Model):
    index = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    description = db.Column(db.String(120))


db.create_all()


@app.route("/")
def index():
    return "This is project work for ECS781 group 10"


@app.route("/mylibrary")
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {
            "index": book.index,
            "title": book.title,
            "author": book.author,
            "description": book.description
        }
        output.append(book_data)
    return {"Library List": output}


@app.route("/mylibrary/<index>", methods=["GET"])
def get_book(index):
    book = Book.query.get_or_404(index)
    return {
            "index": book.index,
            "title": book.title,
            "author": book.author,
            "description": book.description
    }


@app.route("/mylibrary", methods=["POST"])
def add_book():
    book = Book(
        title=request.json["title"],
        author=request.json["author"],
        description=request.json["description"]
    )
    db.session.add(book)
    db.session.commit()
    return {"index": book.index}

@app.route("/mylibrary/<index>", methods=["DELETE"])
def del_book(index):
    book = Book.query.get(index)
    db.session.delete(book)
    db.session.commit()
    return {"message": "item deleted successfully"}

@app.route("/mylibrary/<index>", methods=["PATCH"])
def edit_book(index):
    pass

if __name__ == "__main__":
    app.run(debug=True)
