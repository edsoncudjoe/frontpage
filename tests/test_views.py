
from fl_prt import create_app
import unittest


class FlaskTest(unittest.TestCase):

    def setUp(self):
        app = create_app('dev')
        app.config['TESTING'] = True
        self.app = app.test_client()


#    def test_index(self):
#        testr = app.test_client(self)
#        resp = testr.get('/', content_type='html/text')
#        self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()


