import requests

# Define the URL and the request payload
url = "http://localhost:5678/EstimateHours"
payload = {
    "firstName": "George",
    "lastName": "King",
    "address": "7123 Something Ave.",
    "caseNumber": "128792"
}

print('Sending request with following: ')
print(payload)

# Send a POST request
response = requests.post(url, json=payload)

# Print the response
if response.status_code == 200:
    print("Response received:")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
