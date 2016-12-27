var should = require('chai').should(),
expect = require('chai').expect,
supertest = require('supertest'),
api = supertest('http://front');

describe('API', function () {
  it('should be able to delete the whole catalog', function(done) {
      // FOR TESTING PURPOSES ONLY to run test from same set-up without using fixtures
      done();
  });

    /*
  it('should get empty list of articles', function(done) {
    api.get('/article').end(function(err, res) {
      expect(res.statusCode).to.equal(200);
      expect(res.text).to.equal('{}');
      done();
    });
  });


  it('should be able to add an article', function(done) {
    api.post('/article')
    .send({content: 'foo'}).end(function(err, res) {
      expect(res.statusCode).to.equal(200);
      expect(res.text).to.equal('foo');
      done();
    });
  });

  it('should be not add article with false data', function(done) {
      done();
  });

  it('should be able to get list of articles containing one item', function(done) {
      done();
  });

  it('should be able to read article', function(done) {
      api.get('/article/1').end(function(err, res) {
          expect(res.statusCode).to.equal(200);
          expect(res.headers['content-type']).to.equal('application/json');
          //expect(res.text).to.equal('1');
          done();
      });
  });

  it('should not find non-existent article', function(done) {
      done();
  });

  it('should be able to modify newly added article and return changed data', function(done) {
      done();
  });

  it('should not modify article with same data already existing', function(done) {
      done();
  });

  it('should not be able to delete article that does not exist', function(done) {
      done();
  });

  it('should be able to delete article', function(done) {
      done();
  });

  it('should get empty list of articles', function(done) {
      done();
  });
    */

});
