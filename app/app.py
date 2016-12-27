from flask import Flask, request, jsonify
app = Flask(__name__)

article = {
    'id': 1,
    'title': 'Hello world!',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
}

# Retrieve a list of articles
@app.route('/article', methods = ['GET'])
def list_articles():
    return '{}';

# Retrieve article
@app.route('/article/<int:articleId>', methods = ['GET'])
def get_article(articleId):
    return jsonify([article]);

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
