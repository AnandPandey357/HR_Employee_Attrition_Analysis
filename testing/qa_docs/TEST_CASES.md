# Test Cases - HR Employee Attrition Analysis Dashboard

## Document Information
- **Project Name**: HR Employee Attrition Analysis Dashboard
- **Document Version**: 1.0
- **Test Suite**: Functional & UI Testing

## 1. Functional Test Cases - Data Processing

### TC-001: Data Preprocessing - Missing Value Handling
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-001 |
| **Title** | Verify missing value handling in data preprocessing |
| **Description** | Ensure the preprocessing script correctly handles missing values in the dataset |
| **Preconditions** | Raw dataset with missing values loaded |
| **Test Steps** | 1. Run data_preprocessing.py<br>2. Check for missing values in output<br>3. Verify missing values are filled |
| **Expected Result** | Missing values filled with median (numerical) or mode (categorical) |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-002: Data Preprocessing - Duplicate Removal
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-002 |
| **Title** | Verify duplicate record removal |
| **Description** | Ensure the preprocessing script removes duplicate employee records |
| **Preconditions** | Raw dataset with duplicate records |
| **Test Steps** | 1. Add duplicate records to dataset<br>2. Run data_preprocessing.py<br>3. Verify duplicates removed |
| **Expected Result** | Duplicate records removed, unique records retained |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-003: Data Preprocessing - Categorical Encoding
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-003 |
| **Title** | Verify categorical variable encoding |
| **Description** | Ensure categorical variables are properly encoded for analysis |
| **Preconditions** | Raw dataset loaded |
| **Test Steps** | 1. Run data_preprocessing.py<br>2. Check encoded columns<br>3. Verify encoding mappings |
| **Expected Result** | Categorical columns encoded with consistent mappings |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

## 2. Functional Test Cases - API Endpoints

### TC-004: API - GET Home Endpoint
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-004 |
| **Title** | Verify API home endpoint returns correct information |
| **Description** | Test GET / endpoint returns API information and available endpoints |
| **Preconditions** | Flask server running on localhost:5000 |
| **Test Steps** | 1. Send GET request to http://localhost:5000/<br>2. Verify status code is 200<br>3. Verify response has message and endpoints fields |
| **Expected Result** | Status 200, response contains message and endpoints |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-005: API - GET All Employees
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-005 |
| **Title** | Verify GET /employees returns all employee data |
| **Description** | Test GET /employees endpoint returns complete employee dataset |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /employees<br>2. Verify status code is 200<br>3. Verify response has data array<br>4. Verify data has required fields |
| **Expected Result** | Status 200, data array with all employee records |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-006: API - GET Employee by ID
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-006 |
| **Title** | Verify GET /employees/<id> returns specific employee |
| **Description** | Test GET /employees/<id> endpoint returns correct employee record |
| **Preconditions** | Flask server running, valid employee ID exists |
| **Test Steps** | 1. Send GET request to /employees/EMP001<br>2. Verify status code is 200<br>3. Verify EmployeeID matches request |
| **Expected Result** | Status 200, employee record with correct ID |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-007: API - GET Invalid Employee ID
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-007 |
| **Title** | Verify GET /employees/<invalid-id> returns 404 |
| **Description** | Test edge case: invalid employee ID returns 404 error |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /employees/INVALID999<br>2. Verify status code is 404<br>3. Verify error message in response |
| **Expected Result** | Status 404, error message returned |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-008: API - Filter by Department
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-008 |
| **Title** | Verify department filter functionality |
| **Description** | Test GET /employees?department=Sales filters correctly |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request with department parameter<br>2. Verify status code is 200<br>3. Verify all results are from specified department |
| **Expected Result** | Status 200, all employees from specified department |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-009: API - Get Attrition Statistics
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-009 |
| **Title** | Verify GET /attrition-stats returns comprehensive statistics |
| **Description** | Test GET /attrition-stats endpoint returns all required statistics |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /attrition-stats<br>2. Verify status code is 200<br>3. Verify response has overall, by_department, overtime_impact |
| **Expected Result** | Status 200, comprehensive attrition statistics |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-010: API - Get KPI Metrics
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-010 |
| **Title** | Verify GET /kpi-metrics returns correct KPI data |
| **Description** | Test GET /kpi-metrics endpoint returns all KPI fields |
| **Preconditions** | Flask server running |
| **Test Steps** | 1. Send GET request to /kpi-metrics<br>2. Verify status code is 200<br>3. Verify all KPI fields present and valid |
| **Expected Result** | Status 200, all KPI metrics with valid values |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

## 3. UI Test Cases - Dashboard

### TC-011: Dashboard - Page Loading
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-011 |
| **Title** | Verify dashboard page loads correctly |
| **Description** | Test that the dashboard HTML page loads without errors |
| **Preconditions** | Dashboard file exists at dashboard/index.html |
| **Test Steps** | 1. Open dashboard in browser<br>2. Verify page title<br>3. Verify header displayed<br>4. Verify heading displayed |
| **Expected Result** | Page loads with correct title, header, and heading |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-012: Dashboard - KPI Cards Display
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-012 |
| **Title** | Verify KPI cards display with correct data |
| **Description** | Test that all 4 KPI cards are displayed with valid data |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Verify Total Employees card displayed<br>2. Verify Attrition Rate card displayed<br>3. Verify Average Salary card displayed<br>4. Verify Average Satisfaction card displayed<br>5. Verify values are non-zero |
| **Expected Result | All 4 KPI cards displayed with valid data |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-013: Dashboard - Charts Rendering
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-013 |
| **Title** | Verify all charts render correctly |
| **Description** | Test that all 4 charts are rendered on the dashboard |
| **Preconditions** | Dashboard loaded, JavaScript executed |
| **Test Steps** | 1. Verify Department Chart rendered<br>2. Verify Salary Chart rendered<br>3. Verify Overtime Chart rendered<br>4. Verify Satisfaction Chart rendered |
| **Expected Result** | All 4 charts displayed correctly |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-014: Dashboard - Filter Functionality
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-014 |
| **Title** | Verify department filter works correctly |
| **Description** | Test that department filter filters employee table correctly |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Note initial employee count<br>2. Select "Sales" from department filter<br>3. Click "Apply Filters"<br>4. Verify table shows only Sales employees<br>5. Click "Reset"<br>6. Verify original count restored |
| **Expected Result** | Filter works correctly, reset restores data |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-015: Dashboard - Employee Table Data
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-015 |
| **Title** | Verify employee table contains valid data |
| **Description** | Test that employee table displays correct data with proper formatting |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Verify table has 9 columns<br>2. Verify Employee ID format (EMP###)<br>3. Verify Age is numeric<br>4. Verify Attrition badge displayed |
| **Expected Result** | Table has correct columns and valid data |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-016: Dashboard - Responsive Design
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-016 |
| **Title** | Verify dashboard is responsive |
| **Description** | Test dashboard displays correctly on different screen sizes |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Test at 1920x1080 (Desktop)<br>2. Test at 768x1024 (Tablet)<br>3. Test at 375x667 (Mobile)<br>4. Verify header and KPI cards visible on all sizes |
| **Expected Result** | Dashboard displays correctly on all screen sizes |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-017: Dashboard - Insights Section
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-017 |
| **Title** | Verify insights section is populated |
| **Description** | Test that insights section displays business insights |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Verify insights container displayed<br>2. Verify insight cards present<br>3. Verify each card has title and text |
| **Expected Result** | Insights section populated with business insights |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Medium |

### TC-018: Dashboard - UI Interactivity
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-018 |
| **Title** | Verify UI elements are interactive |
| **Description** | Test that dropdowns and buttons are clickable and enabled |
| **Preconditions** | Dashboard loaded |
| **Test Steps** | 1. Click department dropdown<br>2. Click job role dropdown<br>3. Verify Apply button enabled<br>4. Verify Reset button enabled |
| **Expected Result** | All UI elements are interactive |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | Low |

## 4. EDA Test Cases

### TC-019: EDA - Overtime vs Attrition Analysis
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-019 |
| **Title** | Verify overtime vs attrition analysis |
| **Description** | Test that EDA script correctly analyzes overtime impact on attrition |
| **Preconditions** | Processed data available |
| **Test Steps** | 1. Run eda_analysis.py<br>2. Check overtime vs attrition output<br>3. Verify calculations correct |
| **Expected Result** | Correct attrition rates for overtime vs non-overtime |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

### TC-020: EDA - Salary vs Attrition Analysis
| Field | Details |
|-------|---------|
| **Test Case ID** | TC-020 |
| **Title** | Verify salary vs attrition analysis |
| **Description** | Test that EDA script correctly analyzes salary impact on attrition |
| **Preconditions** | Processed data available |
| **Test Steps** | 1. Run eda_analysis.py<br>2. Check salary vs attrition output<br>3. Verify quartile calculations |
| **Expected Result** | Correct attrition rates by salary quartile |
| **Actual Result** | |
| **Status** | To be executed |
| **Priority** | High |

## Test Summary

| Category | Total | Passed | Failed | Pending |
|----------|-------|--------|--------|---------|
| Data Processing | 3 | 0 | 0 | 3 |
| API Endpoints | 7 | 0 | 0 | 7 |
| Dashboard UI | 8 | 0 | 0 | 8 |
| EDA Analysis | 2 | 0 | 0 | 2 |
| **Total** | **20** | **0** | **0** | **20** |

## Test Execution Notes

- All test cases to be executed in sequence
- Postman collection for API tests (TC-004 to TC-010)
- Selenium scripts for UI tests (TC-011 to TC-018)
- Python scripts for data and EDA tests (TC-001 to TC-003, TC-019 to TC-020)
