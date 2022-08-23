import prettytable
from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.orm import declarative_base, sessionmaker, Query
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



create table User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    age INTEGER NOT NULL,
    email VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL

)


create table Offer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    executor_id INTEGER FOREIGN KEY REFERENCED Order (executor_id) NOT NULL

)

create table Order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(20) NOT NULL,
    description VARCHAR(20) NOT NULL,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    adress VARCHAR(20) NOT NULL,
    price INTEGER NOT NULL,
    customer_id INTEGER NOT NULL,
    executor_id INTEGER FOREIGN KEY REFERENCED Offer(executor_id) NOT NULL

)


@app.route('/users/')
def get_all_users() -> list[dict]:
    with open('Users.json', 'w', encoding='utf-8') as users_file:
        return json.load(users_file)

@app.route('/users/<int:id>')
def get_user_by_id(id: int) -> dict:
    for user in get_all_users():
        if id == user['id']:
            return user
    return {}


@app.route('/orders/')
def get_all_orders() -> list[dict]:
    with open('Orders.json', 'w', encoding='utf-8') as orders_file:
        return json.load(orders_file)


@app.route('/orders/<int:id>')
def get_order_by_id(id: int) -> dict:
    for order in get_all_orders():
        if id == order['id']:
            return order
    return {}

@app.route('/offers/')
def get_all_offers() -> list[dict]:
    with open('Offers.json', 'w', encoding='utf-8') as offers_file:
        return json.load(offers_file)

@app.route('/offers/<int:id>')
def get_offer_by_id(id: int) -> dict:
    for offer in get_all_offers():
        if id == offer['id']:
            return offer
    return {}




@app.route('/users/')
def add_user(user):
    response = requests.post('/', json={"key": "value"})

Class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role  = db.Column(db.String(50))
    phone  = db.Column(db.String(50))

db.create_all()

if __name__ == '__main__':
    app.run(port=2000, debug=True)
