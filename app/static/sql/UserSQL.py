from app import db


def select_all():
    return db.engine.execute("SELECT * FROM User")
