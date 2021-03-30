from flaskshoes.ext.database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'email', self.email
        yield 'password', self.password

    def __repr__(self):
        return '<User %r>' % self.name
