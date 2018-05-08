from app import db
import datetime


def select_daily_posts(id=None):
    day = str(datetime.datetime.today()).split()[0]
    if id is not None:
        return db.engine.execute("SELECT * FROM posts WHERE post_time >= '" + day + "\' AND post_id = " + id)
    else:
        return db.engine.execute("SELECT * FROM posts WHERE post_time >= '" + day + "\'")


def select_weekly_posts(id=None):
    last_week = str(datetime.datetime.today() - datetime.timedelta(days=7))
    if id is not None:
        return db.engine.execute("SELECT * FROM posts WHERE post_time >= '" + last_week + "\' AND post_id = " + id)
    else:
        return db.engine.execute("SELECT * FROM posts WHERE post_time >= '" + last_week + "\'")

