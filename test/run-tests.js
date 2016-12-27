var should = require('chai').should(),
expect = require('chai').expect,
supertest = require('supertest'),
api = supertest('http://front');

describe('API', function () {
  it('should return a 200 response', function(done) {
    api.get('/')
      .expect(200, done);
  });
});
