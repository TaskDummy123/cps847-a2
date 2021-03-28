from app import app
import unittest
import json
import app as calculations 

class FlaskTest(unittest.TestCase):

    # check if reposnding 
    def test_response(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if function return type josn 
    def test_json_content(self):
        tester = app.test_client(self)
        response = tester.get('/io')
        self.assertEqual(response.content_type, 'application/json')


    # check if function return html website
    def test_website_content(self):
        tester = app.test_client(self)
        response = tester.get('/')

        self.assertEqual(response.content_type, 'text/html; charset=utf-8')


    def test_add(self):
        self.assertEqual(calculations.add(1,2), 3)
        self.assertEqual(calculations.add(2,1), 3)
        self.assertEqual(calculations.add(0,2), 2)
        self.assertEqual(calculations.add(1,-1), 0)


    def test_subtract(self):
        self.assertEqual(calculations.subtract(1,2), -1)
        self.assertEqual(calculations.subtract(2,1), 1)
        self.assertEqual(calculations.subtract(4,0), 4)
        self.assertEqual(calculations.subtract(1,-1), 2)
        self.assertEqual(calculations.subtract(-1,2), -3)


    def test_multiply(self):
        self.assertEqual(calculations.multiply(1,2), 2)
        self.assertEqual(calculations.multiply(2,1), 2)
        self.assertEqual(calculations.multiply(1,0), 0)
        self.assertEqual(calculations.multiply(1,-4), -4)
        self.assertEqual(calculations.multiply(-1,-5), 5)



if __name__ == '__main__':
    unittest.main()