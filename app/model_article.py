from app import db

class Article(db.Model):

    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(120), nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, topic, text):
        if not topic:
            raise ValueError('Topic cannot be empty.')
        if not text:
            raise ValueError('Text cannot be empty.')

        self.topic = topic
        self.text = text

    def to_json(self):
        return dict(id=self.id,
                topic=self.topic,
                text=self.text
                )
