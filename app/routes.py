from app import models,db
from flask import current_app as app, jsonify


@app.route('/users')
def get_all_users():

    users = db.session.query(models.User).all()

    return jsonify([user.dict_template() for user in users])


@app.route('/users/<int:uid>')
def get_user_by_id(uid):
    users = db.session.query(models.User).filter(models.User.id == uid).all()

    return jsonify([user.dict_template() for user in users])