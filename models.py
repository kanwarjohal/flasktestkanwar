from app import db
from sqlalchemy.dialects.postgresql import JSON


class Loading(db.Model):
    __tablename__ = 'loading'

    id = db.Column(db.Integer, primary_key=True)
    loading_type = db.Column(db.String())
    loading = db.Column(db.String)

    def __init__(self, loading_type, loading):
        self.loading_type = loading_type
        self.loading = loading

    def __repr__(self):
        return '<id {}>'.format(self.id)