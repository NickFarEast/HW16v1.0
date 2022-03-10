from app import models, db
from flask import current_app as app, jsonify, request,abort



@app.route('/users')
def get_all_users():
    users = db.session.query(models.User).all()

    return jsonify([user.dict_template() for user in users])


@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = db.session.query(models.User).filter(models.User.id == user_id).first()

    return jsonify(user.dict_template())


@app.route('/orders')
def get_all_orders():
    orders = db.session.query(models.Order).all()

    return jsonify([order.dict_template() for order in orders])


@app.route('/orders/<int:order_id>')
def get_order_by_id(order_id):
    orders = db.session.query(models.Order).filter(models.Order.id == order_id).first()

    return jsonify([order.dict_template() for order in orders])


@app.route('/offers')
def get_all_offers():
    offers = db.session.query(models.Offer).all()

    return jsonify([offer.dict_template() for offer in offers])


@app.route('/offers/<offer_id>')
def get_offers_by_id(offer_id):
    offer = db.session.query(models.Offer).filter(models.Offer.id == offer_id).first()

    return jsonify(offer.dict_template())


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json

    db.session.add(models.User(**data))
    db.session.commit()

    return {}


@app.route('/users/<int:user_id>', methods=['PUT'])
def change_user(user_id):
    data = request.json

    user = db.session.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        abort(404)

    db.session.query(models.User).filter(models.User.id == user_id).update(data)
    db.session.commit()

    return {}

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    data = request.json

    result = db.session.query(models.User).filter(models.User.id == user_id).delete()

    if result == 0 :
        abort(404)

    db.session.commit()

    return {}