from flask import Flask
from flask import request, jsonify, abort
from config import BaseConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)


from model_article import *
# Instead of calling method below, I'm creating db+credentials at Docker start up
# in ./mariadb/docker-entrypoint-initdb.d/create_tables.sql
#db.create_all()


# Create article
@app.route('/articles', methods = ['POST'])
def add_article():
    topic = None
    text = None
    data = request.json
    if 'topic' in data:
        topic = data['topic']
    if 'text' in data:
        text = data['text']
    try:
        article = Article(topic, text)
    except ValueError as e:
        return abort(400, str(e)) # Bad Request

    db.session.add(article)
    db.session.commit()
    return jsonify(article.to_json()), 201 # Created

# Retrieve a list of articles
@app.route('/articles', methods = ['GET'])
def list_articles():
    articles = Article.query.order_by(Article.id.asc()).all()
    return jsonify(article = [a.to_json() for a in articles]), 200

# Retrieve article
@app.route('/articles/<int:articleId>', methods = ['GET'])
def get_article(articleId):
    article = Article.query.filter_by(id=articleId).first();
    if article is None:
        abort(404)
    return jsonify(article.to_json()), 200 # OK

# Modify article
@app.route('/articles/<int:articleId>', methods = ['PUT'])
def mod_article(articleId):
    article = Article.query.filter_by(id=articleId).first();
    if article is None:
        abort(404)

    isChanged = False;
    data = request.json
    if 'topic' in data and data['topic'] != article.topic:
        isChanged = True
        article.topic = data['topic']
    if 'text' in data and data['text'] != article.text:
        isChanged = True
        article.text = data['text']

    if isChanged == False:
        return '', 304 # Not Modified

    db.session.commit()
    return jsonify(article.to_json()), 200

@app.route('/articles/<int:articleId>', methods = ['DELETE'])
def del_article(articleId):
    article = Article.query.filter_by(id=articleId).first();
    if article is None:
        abort(404)
    db.session.delete(article);
    db.session.commit();
    return '', 204 # No Content

# FOR TESTING PURPOSES ONLY to run tests from same set-up without using fixtures
@app.route('/articles', methods = ['DELETE'])
def del_all_article():
    db.session.commit();
    num_rows = db.session.query(Article).delete()
    db.session.commit()
    if num_rows > 0:
        return jsonify({'count': num_rows}), 200
    return jsonify(''), 204 # No Content


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
