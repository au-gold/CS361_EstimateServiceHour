# Client Assessment and Estimation Service

This microservice estimates the number of personal care hours required for clients based on their assessment data. The service processes client demographic and medical data, factors in various conditions (e.g., health status, mobility, cognitive abilities), and provides an estimate for the number of care hours needed on a monthly basis. The estimated hours are returned to the main program in JSON format.

## Goals

- **Estimate Personal Care Hours:** Based on the client's demographic and assessment data, the service provides an estimated number of personal care hours.
- **Assessment-Based Calculation:** The service factors in specific criteria like medical conditions and physical abilities to ensure accurate estimates.
- **Return Assessment Results:** The service returns the estimated care hours in a standardized JSON format for easy integration with other systems.

## How to Use This Microservice

1. **Run the Microservice**:
   - Use Python to start the microservice:
     ```python estimate_hours.py```
   - This will launch the microservice at `http://localhost:5678`.

2. **API Communication**:
   - The microservice communicates via HTTP.
   - To estimate personal care hours, send a `POST` request to the endpoint: `http://localhost:5678/EstimateHours`.

3. **Request Body Requirements**:
   - The `POST` request body must include, at minimum, a `caseNumber` and its value. This variable is case-sensitive.
   - The microservice will internally generate client condition data for demonstration purposes (this simulates database retrieval based on `caseNumber`).

4. **Example Python Code for API Call**:
   Use the following Python code to call the API and receive the estimated care hours:

   ```python
   import requests

   # Define the URL and the request payload
   url = "http://localhost:5678/EstimateHours"
   payload = {
       "firstName": "George",
       "lastName": "King",
       "address": "7123 Something Ave.",
       "caseNumber": "128792"
   }

   # Send a POST request
   response = requests.post(url, json=payload)

   # Print the response
   if response.status_code == 200:
       print("Response received:")
       print(response.json())
   else:
       print(f"Error: {response.status_code}")

5. **How to Receive Data**
   - The microservice responds with a JSON object containing the estimated personal care hours based on the provided caseNumber.
   - It is a HTTP response with a JSON body containing the requested data.
   - In Python, `response = requests.post(url, json=payload)` will store the JSON to 'response' variable.

7. **Respond Body:**
```json
  {
    "firstName": "George",
    "lastName": "King",
    "address": "7123 Something Ave.",
    "caseNumber": "128792",
    "estimatedMonthlyHour": 150
  }
