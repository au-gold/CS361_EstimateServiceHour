from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Sample condition-based care hours dictionary
condition_hours = {
    "healthy": 40,
    "mobility_issue": 120,
    "paralysis": 200,
    "wheelchair_bound": 180,
    "fall_risk": 100,
    "dementia": 180,
    "alzheimers": 200,
    "mild_cognitive_impairment": 120,
    "depression": 80,
    "schizophrenia": 150,
    "chronic_illness": 150,
    "cancer": 200,
    "heart_failure": 180,
    "respiratory_disease": 160,
    "kidney_disease": 140,
    "terminal_illness": 250,
    "post_surgery": 100,
    "fractures": 120,
    "visual_impairment": 90,
    "hearing_impairment": 70,
    "intellectual_disability": 130,
    "autism_spectrum": 140,
    "elderly_with_multiple_conditions": 180,
    "frailty": 150,
    "osteoporosis": 100,
    "stroke_recovery": 150,
    "diabetes": 110,
    "obesity": 130,
    "hypertension": 70,
    "multiple_sclerosis": 160,
    "epilepsy": 100,
}

# Example of client data mapping based on case number
client_data = {
    "128792": {
        "conditions": ["mobility_issue", "chronic_illness"],  # List of conditions
    },
    # Add other cases as needed
}

# Function to estimate personal care hours
def estimate_care_hours(conditions):
    # Calculate total hours based on conditions
    total_hours = 0
    for condition in conditions:
        if condition in condition_hours:
            total_hours += condition_hours[condition]
    return total_hours

# Define the route for estimating personal care hours
@app.route('/EstimateHours', methods=['POST'])
def estimate_hours():
    start_time = time.time()

    data = request.json

    # Extract case number from the request
    case_number = data.get('caseNumber')

    if case_number not in client_data:
        return jsonify({"error": "Case number not found"}), 400

    # Retrieve client details based on case number
    client = client_data[case_number]

    # Get the client's conditions
    conditions = client.get("conditions", [])

    # Estimate the care hours based on conditions
    estimated_hours = estimate_care_hours(conditions)

    # Prepare the response
    response = {
        "firstName": client["firstName"],
        "lastName": client["lastName"],
        "address": client["address"],
        "caseNumber": case_number,
        "estimatedMonthlyHour": estimated_hours
    }
    
    # Calculate elapsed time for response (for performance requirement)
    elapsed_time = time.time() - start_time
    if elapsed_time > 2:
        return jsonify({"error": "Response time exceeded the 2-second limit"}), 500
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)