from app import db

from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer)
    email = db.Column(db.String(200), unique=True)
    role = db.Column(db.String(200))
    phone = db.Column(db.String(16), unique=True)

    def dict_template(user):

        """
        Serialize implementation
        """
        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "age": user.age,
            "email": user.email,
            "role": user.role,
            "phone": user.phone
        }



class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    customer = relationship('User', foreign_keys='Order.customer_id')
    executor = relationship('User', foreign_keys='Order.executor_id')

    def dict_template(order):

        """
        Serialize implementation
        """
        return {
            "id": order.id,
            "name": order.name,
            "description": order.description,
            "start_date": order.start_date,
            "end_date": order.end_date,
            "address": order.address,
            "price": order.price,
            "customer_id": order.customer_id,
            "executor_id": order.executor_id
        }

class Offer(db.Model):
    __tablename__ = 'offers'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    executor_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    order = relationship('Order')
    executor = relationship('User')

    def dict_template(offer):

        """
        Serialize implementation
        """
        return {
            "id": offer.id,
            "order_id": offer.order_id,
            "executor_id": offer.executor_id
        }

