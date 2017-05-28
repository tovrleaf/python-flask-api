var should = require('chai').should(),
    expect = require('chai').expect,
    supertest = require('supertest'),
    api = supertest('http://front');


describe('API', function () {

  var articleId;

  it('should get empty list of articles', function(done) {
    api.get('/articles').end(function(err, res) {
      expect(res.statusCode).to.equal(200);
      expect(res.headers['content-type']).to.equal('application/json');
      expect(JSON.parse(res.text)).to.deep.equal({'article': []});
      done();
    });
  });

  it('should be able to add an article', function(done) {
    var newArticle = {topic: 'foo', text: 'bar'};

    api.post('/articles')
    .send(newArticle).end(function(err, res) {
      expect(res.statusCode).to.equal(201);
      expect(res.headers['content-type']).to.equal('application/json');

      var createdArticle = JSON.parse(res.text)
      Number.isInteger(createdArticle.id).should.be.true;

      // read id from  result and remove it
      articleId = createdArticle.id;
      delete createdArticle.id;

      expect(createdArticle).to.deep.equal(newArticle);
      done();
    });
  });

  it('should not be add article with insufficient data', function(done) {
      api.post('/articles')
      .send({'topic': 'im not giving text key'}).end(function(err, res) {
        expect(res.statusCode).to.equal(400);
        done();
      });
  });

  it('should be able to get list of articles containing one item', function(done) {
    api.get('/articles').end(function(err, res) {
      expect(res.statusCode).to.equal(200);
      expect(res.headers['content-type']).to.equal('application/json');

      var articles = JSON.parse(res.text).article;
      expect(articles.length).to.equal(1);

      // verify that the article has required fields
      expect(articles[0]).to.have.deep.property('id');
      expect(articles[0]).to.have.deep.property('topic');
      expect(articles[0]).to.have.deep.property('text');
      done();
    });
  });

  it('should be able to read article', function(done) {
      api.get('/articles/' + articleId).end(function(err, res) {
          expect(res.statusCode).to.equal(200);
          expect(res.headers['content-type']).to.equal('application/json');

          var article = JSON.parse(res.text);
          // verify that the article has required fields
          expect(article).to.have.deep.property('id');
          expect(article).to.have.deep.property('topic');
          expect(article).to.have.deep.property('text');
          done();
      });
  });

  it('should not find non-existent article', function(done) {
    api.get('/articles/0').end(function(err, res) {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });

  it('should be able to modify newly added article and return changed data', function(done) {
       var newContent = 'new Content text';

       api.put('/articles/' + articleId).send({'text': newContent}).end(function (err, res) {
         expect(res.statusCode).to.equal(200);
         expect(res.headers['content-type']).to.equal('application/json');
         var modifiedArticle = JSON.parse(res.text);
         expect(modifiedArticle).to.deep.equal(
           {
             'id': articleId,
             'topic': modifiedArticle.topic,
             'text': newContent
           }
         );
         done();
      });
  });

  it('should not modify article with same data already existing', function(done) {
      api.get('/articles/' + articleId).end(function(err, res) {
        var article = JSON.parse(res.text);
         api.put('/articles/' + articleId).send(
           {
             'topic': article.topic,
             'text': article.text
           }).end(function (err, res) {
             expect(res.statusCode).to.equal(304);
             done();
           });
      });
  });

  it('should not be able to modify article that does not exist', function(done) {
      api.get('/articles/0').end(function(err, res) {
        expect(res.statusCode).to.equal(404);
        done();
      });
  });

  it('should not be able to delete article that does not exist', function(done) {
      api.delete('/articles/0').end(function(err, res) {
        expect(res.statusCode).to.equal(404);
        done();
      });
  });

  it('should be able to delete article', function(done) {
      api.delete('/articles/' + articleId).end(function(err, res) {
        expect(res.statusCode).to.equal(204);
        done();
      });
  });

});
