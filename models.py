"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


class User(db.Model):

    __tablename__ = "users"
# NOT SURE SURE WHAT IS GOING ON HERE, COPIED FROM SOLUTION AND ArgumentError appears
    id = db.Column(int, primary_key=True)
    first_name = db.Column(text, nullable=False)
    last_name = db.Column(text, nullable=False)
    image_url = db.Column(text, nullable=False, default=DEFAULT_IMAGE_URL)

    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)
