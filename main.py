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

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    email = db.Column(db.String(50))
    role  = db.Column(db.String(50))
    phone  = db.Column(db.String(50))


class Offer(db.Model):
    __tablename__ = "offers"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    last_name = db.Column(db.String(20))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    description = db.Column(db.String(200))
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    adress = db.Column(db.String(200))
    price = (db.Integer)
    customer_id = db.Column(db.String(200))
    executor_id = db.Column(db.Integer, db.ForeignKey("users.id"))


@app.route('/users/', methods=['GET', 'POST'])
def get_all_users():
    with open('Users.json', 'w', encoding='utf-8') as users_file:
    if request.method == "POST":
        data = request.json
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return "", 201
    return json.load(users_file)



@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_user_by_id(id: int):
    if request.method == "PUT":
      data = requests.json
      user = db.session.query(User).get(id)

      user.id = data.get("id")
      user.first_name = data.get("first_name")
      user.last_name = data.get("last_name")
      user.age = data.get("age")
      user.email = data.get("email")
      user.role = data.get("role")
      user.phone = data.get("phone")

      db.session.add(user)
      db.session.commit()
      return "", 204

""" 
@app.route('/users/<int:id>')
def get_user_by_id(id: int) -> dict:
    for user in get_all_users():
        if id == user['id']:
            return user
    return {}
"""

@app.route('/orders/')
def get_all_orders() -> list[dict]:
    with open('Orders.json', 'w', encoding='utf-8') as orders_file:
        if request.method == "POST":
            data = request.json
            order = Order(**data)
            db.session.add(order)
            db.session.commit()
            return "", 201
        return json.load(orders_file)


@app.route('/orders/<int:id>')
def get_order_by_id(id: int) -> dict:
    if request.method == "PUT":
      data = requests.json
      order = db.session.query(Order).get(id)
      order.id = data.get("order")
      order.order_id = data.get("order")
      order.last_name = data.get("order")
      order.executor_id = data.get("order")

      db.session.add(offer)
      db.session.commit()
      return "", 204



@app.route('/offers/')
def get_all_offers() -> list[dict]:
    with open('Offers.json', 'w', encoding='utf-8') as offers_file:
        if request.method == "POST":
            data = request.json
            offer = Offer(**data)
            db.session.add(offer)
            db.session.commit()
            return "", 201
        return json.load(offers_file)

@app.route('/offers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer_by_id(id: int) -> dict:
    if request.method == "PUT":
      data = requests.json
      offer = db.session.query(Offer).get(id)
      offer.id = data.get("offer")
      offer.order_id = data.get("offer")
      offer.last_name = data.get("offer")
      offer.executor_id = data.get("offer")

      db.session.add(offer)
      db.session.commit()
      return "", 204

@app.route('/users/', methods=['POST', 'PUT', 'DELETE'])
def add_user(user):
    max = User(id=3, order_id = 100, last_name='max', executor_id = 32)

    if request.method == "POST":
      data = requests.json
      user = db.session.query(User).get(id)
      user.id = data.get("user")
      user.order_id = data.get("user")
      user.last_name = data.get("user")
      user.executor_id = data.get("user")


    db.session.add(user)
    db.session.commit()

    if request.method == "PUT":
      data = requests.json
      user = db.session.query(User).get(id)
      user.id = data.get("user")
      user.order_id = data.get("user")
      user.last_name = data.get("user")
      user.executor_id = data.get("user")

      db.session.add(user)
      db.session.commit()

    if request.method == "DELETE":
        data = requests.json
        user = db.session.query(User).get(id)
        user.id = data.get("user")
        user.order_id = data.get("user")
        user.last_name = data.get("user")
        user.executor_id = data.get("user")


        db.session.query(user).delete()
        db.session.commit()


db.create_all()

if __name__ == '__main__':
    app.run(port=2000, debug=True)
