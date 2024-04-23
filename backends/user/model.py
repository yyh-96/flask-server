from common.db_extension import db

class UserModel(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64))
    more = db.Column(db.String(255))
    face_encoding = db.Column(db.String(4096))

    def __repr__(self):
        return {"name": self.name, "more": self.more}