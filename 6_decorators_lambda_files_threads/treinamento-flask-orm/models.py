from flask_sqlalchemy import SQLAlchemy
from server import app

db_password = ""

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:{}@localhost/treinamento_db'.format(db_password)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    image_link = db.Column(db.String(1000))

    def __init__(self, email, username="", image_link=""):
        self.username = username
        self.email = email
        self.image_link = image_link

    def insert(self):
        db.session.add(self)
        db.session.commit()
