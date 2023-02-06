import unittest
from methods import Token, Restricted
from werkzeug import exceptions



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()


    def test_generate_token(self):
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))

    def test_access_token_bob(self):
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidmlld2VyIn0.l7pxJXYHlJdtI9RME2UesMzuVjqf-RtzQeLTHomo_Ic', self.convert.generate_token('bob', 'thisIsNotAPasswordBob'))
    
    def test_check_role_exists(self):
        with self.assertRaises(exceptions.Forbidden):
            self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiTk9ORSJ9.AxA08Nf3JLoxjlXsIVv0BeHE4tVSEs-u60gJDm2Dk4U')

        

if __name__ == '__main__':
    unittest.main()
