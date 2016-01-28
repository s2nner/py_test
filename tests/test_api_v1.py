from api import create_app
import unittest
import flask
import json
import api.auth

from werkzeug.exceptions import BadRequest



class APIV1TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(environment="Testing")


    def test_signin_version(self):
        user = "name"
        ujson = json.dumps(dict(type='simple', user="user", pswd="q"))
        # ujson = dict(type='simple',user="user", pswd="q")
        req = self.app.test_client().post('/api/v1/auth/signin', data=ujson, content_type='application/json' ).data
        data = json.loads(req.decode('utf-8'))
        assert data.get('result') == True


if __name__ == '__main__':
    unittest.main()
