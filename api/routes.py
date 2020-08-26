# exemplo
from flask import Flask, jsonify, request, abort, make_response
from api import app

books = ["A", "B", "C", "D", "E", "F", "G"]

@app.route('/')
def home():
    return 'my flask api'

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<string:book_id>', methods=['GET'])
def get_book(book_id):
    for book in books:
        if book_id == book:
            return book

@app.route('/books/<string:book>', methods=['POST'])
def create_book(book):
    books.append(book)
    return jsonify(books)

@app.route('/books/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    books.remove(book_id)
    return jsonify(books)
