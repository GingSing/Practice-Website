from app import db
import datetime


# create new POST
def create_post(title, subtitle, content, id):
    now = datetime.datetime.today()
    insert_statement = """INSERT INTO posts(post_title, post_subtitle, post_content, post_time, company_id) " \
                       "VALUES( %s, %s, %s, %s, %s)""", (title, subtitle, content, str(now), id)
    return db.engine.execute(insert_statement)