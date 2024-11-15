import unittest
from flask import Flask, json
from estimate_hours import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_estimate_hours(self):
        """Test the /EstimateHours endpoint."""
        # Prepare a sample JSON body
        data = {
            "firstName": "George",
            "lastName": "King",
            "caseNumber": "12345",
            "dob": "1999-01-01",
            "gender": "Male",
            "language": "English",
            "residentalAddress": "1234 Somewhere Ave.",
            "mailingAddress": "Same",
            "phonenumber": "123456789",
            "collateralFirstName": "Somename",
            "collateralLastName": "SomeLastname",
            "relation": "Friend",
            "collateralPhone": "123456789",
            "collateralEmail": "coll@coll.com"
        }

        # Send a POST request to the /EstimateHours route
        response = self.app.post('/EstimateHours', 
                                 data=json.dumps(data),
                                 content_type='application/json')

        # Assert the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Get the JSON response
        response_data = response.get_json()

        # Assert that the response contains the expected keys
        self.assertIn('caseNumber', response_data)
        self.assertIn('estimatedMonthlyHour', response_data)
        print(response_data)

        # Assert that the estimated monthly hours is an integer
        self.assertIsInstance(response_data['estimatedMonthlyHour'], int)

    def tearDown(self):
        """Clean up after each test."""
        pass

if __name__ == '__main__':
    unittest.main()
