from app import models, db
from flask import current_app as app, jsonify, request, abort
from datetime import datetime


@app.route('/users')
def get_all_users():
    """Функция для отображения всех пользователей в базе"""

    users = db.session.query(models.User).all()

    return jsonify([user.dict_template() for user in users])


@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    """Функция для отображения одного пользователя по номеру id"""

    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    return jsonify(user.dict_template())


@app.route('/orders')
def get_all_orders():
    """Функция для отображения всех заказов в базе"""

    orders = db.session.query(models.Order).all()

    return jsonify([order.dict_template() for order in orders])


@app.route('/orders/<int:order_id>')
def get_order_by_id(order_id):
    """Функция для отображения одного заказа по номеру id"""

    orders = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    return jsonify([order.dict_template() for order in orders])


@app.route('/offers')
def get_all_offers():
    """Функция для отображения всех предложений в базе"""

    offers = db.session.query(models.Offer).all()

    return jsonify([offer.dict_template() for offer in offers])


@app.route('/offers/<offer_id>')
def get_offers_by_id(offer_id):
    """Функция для отображения одного предложения по id"""

    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    return jsonify(offer.dict_template())


@app.route('/users', methods=['POST'])
def create_user():
    """Функция для создания нового пользователя в базе"""

    data = request.json

    db.session.add(models.User(**data))
    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['PUT'])
def change_user(user_id):
    """Функция для внесения изменений в информацию о пользователе по id """
    data = request.json

    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Функция для удаления пользователя из базы по id"""

    result = db.session.query(models.User).filter(models.User.id == user_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}


@app.route('/orders', methods=['POST'])
def create_order():
    """Функция для создания нового заказа в базе"""

    data = request.json

    for name, value in data.items():
        if isinstance(value, str) and value.count('/') == 2:
            data[name] = datetime.strptime(value, '%m/%d/%Y')

    db.session.add(models.Order(**data))
    db.session.commit()

    return {}


@app.route('/orders/<int:order_id>', methods=['PUT'])
def change_order(order_id):
    """Функция для внесения изменений в информацию о заказе по id """
    data = request.json

    order = db.session.query(models.Order).filter(models.Order.id == order_id).first()
    if order is None:
        abort(404)

    db.session.query(models.Order).filter(models.Order.id == order_id).update(data)
    db.session.commit()

    return {}


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    """Функция для удаления заказа из базы по id"""
    result = db.session.query(models.Order).filter(models.Order.id == order_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}


@app.route('/offers', methods=['POST'])
def create_offer():
    """Функция для создания нового предложения в базе"""

    data = request.json

    db.session.add(models.Offer(**data))
    db.session.commit()

    return {}


@app.route('/offers/<int:offer_id>', methods=['PUT'])
def change_offer(offer_id):
    """Функция для внесения изменений в информацию о предложении по id """
    data = request.json

    user = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()
    if user is None:
        abort(404)

    db.session.query(models.Offer).filter(models.Offer.id == offer_id).update(data)
    db.session.commit()

    return {}


@app.route('/offers/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    """Функция для удаления предложения из базы по id"""

    result = db.session.query(models.Offer).filter(models.Offer.id == offer_id).delete()

    if result == 0:
        abort(404)

    db.session.commit()

    return {}

