import os
import json

from datetime import datetime

from app import db, models


def load_fixture(file_path):
    content = []
    if os.path.isfile(file_path):
        with open(file_path, encoding="utf-8") as file:
            content = json.load(file)

    return content


def migrate_users(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for user in fixture_content:

        if db.session.query(models.User).filter(models.User.id == user['id']).first() is None:
            db.session.add(models.User(**user))

    db.session.commit()


def migrate_orders(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for order in fixture_content:

        for field_name, field_value in order.items():
            if isinstance(field_value, str) and field_value.count('/') == 2:
                order[field_name] = datetime.strptime(field_value, '%m/%d/%Y')

        if db.session.query(models.Order).filter(models.Order.id == order['id']).first() is None:
            db.session.add(models.Order(**order))

    db.session.commit()


def migrate_offers(fixture_path):
    fixture_content = load_fixture(fixture_path)

    for offer in fixture_content:

        if db.session.query(models.Offer).filter(models.Offer.id == offer['id']).first() is None:
            db.session.add(models.Offer(**offer))

    db.session.commit()