from app import db

class Article(db.Model):

    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(120), nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, topic, text):
        self.topic = topic
        self.text = text
