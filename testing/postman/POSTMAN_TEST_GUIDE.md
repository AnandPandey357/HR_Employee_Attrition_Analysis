# Postman API Testing Guide

## Overview
This document provides instructions for testing the HR Employee Attrition Analysis API using Postman.

## Prerequisites
- Postman installed (https://www.postman.com/downloads/)
- Flask API server running on http://localhost:5000

## Setup Instructions

### 1. Start the API Server
```bash
cd api
pip install -r requirements.txt
python app.py
```

### 2. Import the Collection
1. Open Postman
2. Click "Import" in the top left
3. Select `hr_attrition_collection.json` from `testing/postman/`
4. The collection will be imported with all test cases

### 3. Configure Environment Variables
The collection uses a variable `{{base_url}}` set to `http://localhost:5000`. 
If your server runs on a different port, update this variable:
- Click the gear icon (Manage Environments)
- Edit the base_url variable

## Test Cases Overview

| Test Case | Endpoint | Purpose | Validation |
|-----------|----------|---------|------------|
| API Home | GET / | Verify API is running | Status 200, response has message & endpoints |
| Get All Employees | GET /employees | Retrieve all employee data | Status 200, data array, required fields |
| Get Employee by ID | GET /employees/EMP001 | Get specific employee | Status 200, correct EmployeeID |
| Invalid Employee ID | GET /employees/INVALID999 | Edge case testing | Status 404, error message |
| Filter by Department | GET /employees?department=Sales | Query parameter test | Status 200, all results from Sales |
| Filter by Attrition | GET /employees?attrition=Yes | Query parameter test | Status 200, all have Attrition=Yes |
| Attrition Statistics | GET /attrition-stats | Get comprehensive stats | Status 200, overall, dept, overtime data |
| KPI Metrics | GET /kpi-metrics | Get KPI data | Status 200, all KPI fields present |
| Department Stats | GET /department-stats | Department breakdown | Status 200, dept data with required fields |
| Salary Statistics | GET /salary-stats | Salary analysis | Status 200, overall, ranges, attrition data |
| Invalid Endpoint | GET /invalid-endpoint | 404 error handling | Status 404, error message |

## Running Tests

### Manual Execution
1. Open the imported collection
2. Click on each request
3. Click "Send" to execute
4. View test results in the "Test Results" tab

### Automated Execution (Collection Runner)
1. Click the collection name
2. Click the "..." menu → "Run collection"
3. Select all requests
4. Click "Run HR Employee Attrition API Collection"
5. View the test results summary

### Expected Results
- All tests should pass (green checkmarks)
- Response time should be < 500ms
- Status codes should be as documented
- Response schema should match expectations

## Test Coverage

### Status Code Validation
- 200: Successful GET requests
- 404: Resource not found (invalid ID, invalid endpoint)
- 500: Internal server error (if data file is missing)

### Schema Validation
- All responses have expected fields
- Data types are correct (numbers, strings, arrays)
- Required fields are present

### Edge Cases Tested
- Invalid employee ID
- Invalid endpoint
- Empty filter results
- Missing data file

## Sample Request/Response

### Request: Get All Employees
```
GET http://localhost:5000/employees
```

### Response
```json
{
  "total": 20,
  "data": [
    {
      "EmployeeID": "EMP001",
      "Age": 32,
      "Gender": "Male",
      "Department": "Sales",
      "JobRole": "Sales Executive",
      "MonthlyIncome": 4500,
      "JobSatisfaction": 3,
      "WorkLifeBalance": 2,
      "Overtime": "Yes",
      "Attrition": "Yes"
    }
  ]
}
```

## Troubleshooting

### Connection Refused
- Ensure Flask server is running
- Check that base_url variable is correct
- Verify port 5000 is not in use

### 404 Errors
- Verify endpoint path is correct
- Check for typos in URL

### Data Not Found
- Ensure CSV file exists at `data/raw/hr_employee_data.csv`
- Check file permissions

## Test Metrics
- Total Test Cases: 11
- Endpoints Covered: 7
- Edge Cases: 3
- Expected Pass Rate: 100%
