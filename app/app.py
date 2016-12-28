from flask import Flask
from flask import request, jsonify
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from model_article import *
# Instead of calling method below, I'm creating db+credentials at Docker start up
# in ./mariadb/docker-entrypoint-initdb.d/create_tables.sql
#db.create_all()


article = {
    'id': 1,
    'title': 'Hello world!',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
}

# Retrieve a list of articles
@app.route('/article', methods = ['GET'])
def list_articles():
    #articles = Article.query.order_by(Post.id.desc()).all()
    articles = Article.query.all()
    return jsonify(articles)

# Retrieve article
@app.route('/article/<int:articleId>', methods = ['GET'])
def get_article(articleId):
    return jsonify([article])

# Create article
@app.route('/article', methods = ['POST'])
def add_article():
    return 'create';

# Modify article
@app.route('/article/<int:articleId>', methods = ['PUT'])
def mod_article(articleId):
    return 'update';

@app.route('/article/<int:articleId>', methods = ['DELETE'])
def del_article(articleId):
    return 'del';


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
