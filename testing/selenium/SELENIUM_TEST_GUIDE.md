# Selenium Automation Test Guide

## Overview
This document provides instructions for running Selenium UI automation tests for the HR Employee Attrition Dashboard.

## Prerequisites
- Python 3.8 or higher
- Chrome browser installed
- Chrome WebDriver (automatically managed by webdriver-manager)

## Setup Instructions

### 1. Install Dependencies
```bash
cd testing/selenium
pip install -r requirements.txt
```

### 2. Verify Dashboard File
Ensure the dashboard HTML file exists at:
```
dashboard/index.html
```

## Running Tests

### Run All Tests
```bash
cd testing/selenium
python test_dashboard.py
```

### Run Specific Test
```bash
cd testing/selenium
pytest test_dashboard.py::TestHRDashboard::test_dashboard_loading -v
```

### Run with HTML Report
```bash
cd testing/selenium
pytest test_dashboard.py --html=../../output/test_report.html --self-contained-html
```

## Test Cases Overview

| Test Case | Description | Validation |
|-----------|-------------|------------|
| Dashboard Loading | Verify page loads correctly | Title, header, heading displayed |
| KPI Cards Display | Verify KPI cards show data | All 4 cards present with valid values |
| Charts Rendering | Verify all charts render | 4 charts displayed correctly |
| Filter Functionality | Test department filter | Filter works, reset works |
| Insights Section | Verify insights populated | Insight cards present with content |
| Employee Table Data | Verify table data validity | Correct columns, valid data formats |
| Responsive Design | Test different screen sizes | Works on desktop, tablet, mobile |
| UI Interactivity | Verify elements clickable | Dropdowns, buttons enabled |
| Last Updated Timestamp | Verify timestamp displayed | Timestamp present and non-empty |
| Footer Elements | Verify footer content | Footer displayed with expected text |

## Test Coverage

### UI Elements Tested
- Header and navigation
- KPI cards (4)
- Charts (4)
- Filter controls (2 dropdowns, 2 buttons)
- Insights section
- Employee table
- Footer

### Functional Areas
- Page loading
- Data display
- Filter functionality
- Responsiveness
- Interactivity

### Browser Compatibility
- Chrome (primary)
- Can be extended for Firefox, Safari, Edge

## Expected Results

### All Tests Should Pass
- 10/10 tests passing
- HTML report generated in `output/test_report.html`
- Execution time: < 30 seconds

### Sample Output
```
=== Test 1: Dashboard Loading ===
✓ Page title verified
✓ Header is displayed
✓ Dashboard heading verified
✓ Test 1 PASSED: Dashboard loads correctly

=== Test 2: KPI Cards Display ===
✓ Total Employees: 20
✓ Attrition Rate: 35.00%
✓ Average Salary: $6,265
✓ Average Satisfaction: 3.2
✓ Test 2 PASSED: All KPI cards displayed correctly

...
```

## Troubleshooting

### Chrome WebDriver Issues
- Ensure Chrome browser is installed
- Check Chrome version compatibility
- webdriver-manager should handle this automatically

### File Not Found Error
- Verify dashboard file path is correct
- Check file permissions

### Tests Timing Out
- Increase implicit wait time in setup
- Check if JavaScript is loading slowly

## Adding New Tests

To add a new test case:

1. Create a new test method in `TestHRDashboard` class
2. Name it starting with `test_`
3. Use Selenium WebDriver methods to interact with elements
4. Add assertions to validate results
5. Add print statements for debugging

Example:
```python
def test_new_feature(self):
    """Test new feature"""
    print("\n=== Test: New Feature ===")
    
    self.driver.get(self.dashboard_url)
    time.sleep(2)
    
    element = self.driver.find_element(By.ID, "elementId")
    assert element.is_displayed(), "Element not found"
    
    print("✓ Test PASSED: New feature works")
```

## Test Metrics
- Total Test Cases: 10
- UI Elements Validated: 20+
- Screen Sizes Tested: 3
- Expected Pass Rate: 100%
