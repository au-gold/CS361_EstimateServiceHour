# Client Assessment and Estimation Service

This microservice estimates the number of personal care hours required for clients based on their assessment data. The service processes client demographic and medical data, factors in various conditions (e.g., health status, mobility, cognitive abilities), and provides an estimate for the number of care hours needed on a monthly basis. The estimated hours are returned to the main program in JSON format.

## Goals

- **Estimate Personal Care Hours:** Based on the client's demographic and assessment data, the service provides an estimated number of personal care hours.
- **Assessment-Based Calculation:** The service factors in specific criteria like medical conditions and physical abilities to ensure accurate estimates.
- **Return Assessment Results:** The service returns the estimated care hours in a standardized JSON format for easy integration with other systems.

## User Stories

### User Story 1: Estimate Personal Care Hours

**As a social worker**, I want the service to estimate the number of personal care hours required based on client needs so that I can make informed decisions on support levels.

**Acceptance Criteria:**
- Given client demographic and assessment data, when the data is submitted to the service, the service should return an estimated number of personal care hours.
- The system should be reliable, with an accuracy of within 5% based on pre-defined assessment factors.
- The system should respond within 2 seconds to ensure timely results for social workers.

### User Story 2: Assessment-Based Calculation

**As a social worker**, I want the service to factor in specific criteria (e.g., medical conditions, physical limitations) in the assessment to ensure the estimate is relevant to the client’s situation.

**Acceptance Criteria:**
- The service factors in each assessment criterion (e.g., health conditions, mobility scores) to calculate the estimated care hours.
- The system should apply weights to each criterion based on pre-defined importance levels.
- The system should respond within 2 seconds to ensure timely results.

### User Story 3: Return Assessment Results

**As a social worker**, I want the service to return the estimated care hours in a format that the main program can easily use, so that I can see the results without additional data processing.

**Acceptance Criteria:**
- The service should return a JSON object containing the estimated care hours.
- The service should ensure interoperability by using a standard JSON format for seamless integration.

## API Endpoint

### `POST /EstimateHours`

- **Description:** This endpoint receives client assessment data and returns the estimated number of personal care hours required based on the conditions and medical history associated with the provided case number.
- **Request Body:**
  ```json
  {
    "firstName": "George",
    "lastName": "King",
    "address": "7123 Something Ave.",
    "caseNumber": "128792"
  }

- **Respond Body:**
  ```json
  {
    "firstName": "George",
    "lastName": "King",
    "address": "7123 Something Ave.",
    "caseNumber": "128792",
    "estimatedMonthlyHour": 150
  }
