# Bug Report Samples - HR Employee Attrition Analysis Dashboard

## Document Information
- **Project Name**: HR Employee Attrition Analysis Dashboard
- **Document Version**: 1.0
- **Purpose**: Sample bug reports for reference

---

## Bug Report #1 - Critical

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-001 |
| **Title** | API server crashes when CSV file is missing |
| **Severity** | Critical |
| **Priority** | P1 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-15 |
| **Assigned To** | Developer |
| **Environment** | Development |

### Description
The Flask API server crashes with a FileNotFoundError when the HR data CSV file is missing from the expected location. The error is not handled gracefully, causing the entire application to fail.

### Steps to Reproduce
1. Navigate to the `data/raw/` directory
2. Delete or rename `hr_employee_data.csv`
3. Start the API server: `python api/app.py`
4. Observe the crash

### Expected Behavior
The API should handle missing data gracefully:
- Return a user-friendly error message
- Log the error appropriately
- Continue running for other endpoints that don't require data

### Actual Behavior
Server crashes immediately with FileNotFoundError traceback.

### Error Message
```
FileNotFoundError: [Errno 2] No such file or directory: '../data/raw/hr_employee_data.csv'
```

### Root Cause
No error handling in the data loading section of `api/app.py`.

### Suggested Fix
Add try-catch block around file loading:
```python
try:
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Loaded {len(df)} employee records")
except FileNotFoundError:
    print(f"⚠ Data file not found at {DATA_PATH}")
    df = pd.DataFrame()
```

### Attachments
- Screenshot of error traceback
- Log file excerpt

---

## Bug Report #2 - High

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-002 |
| **Title** | Dashboard charts not rendering on mobile devices |
| Severity** | High |
| **Priority** | P1 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-16 |
| **Assigned To** | Frontend Developer |
| **Environment** | Production |

### Description
Charts on the dashboard fail to render correctly on mobile devices (screen width < 768px). The canvas elements are present but charts appear blank or distorted.

### Steps to Reproduce
1. Open dashboard in Chrome browser
2. Open DevTools and toggle device toolbar
3. Select mobile device (e.g., iPhone 12 - 390x844)
4. Refresh the page
5. Observe chart rendering

### Expected Behavior
Charts should render correctly on all screen sizes with appropriate scaling and responsiveness.

### Actual Behavior
Charts appear blank, canvas elements are empty, or charts are cut off on mobile view.

### Affected Charts
- Department Chart
- Salary Chart
- Overtime Chart
- Satisfaction Chart

### Root Cause
Chart.js responsive configuration not properly set for mobile viewports.

### Suggested Fix
Update Chart.js configuration:
```javascript
options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            display: true,
            position: 'bottom',
            labels: {
                boxWidth: 10,
                font: {
                    size: 10
                }
            }
        }
    }
}
```

### Attachments
- Screenshots of mobile view
- Browser console logs

---

## Bug Report #3 - Medium

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-003 |
| **Title** | Department filter does not reset employee table correctly |
| **Severity** | Medium |
| **Priority** | P2 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-17 |
| **Assigned To** | Frontend Developer |
| **Environment** | Development |

### Description
After applying a department filter and then clicking the Reset button, the employee table does not restore to show all employees. It continues to show only the filtered results.

### Steps to Reproduce
1. Open dashboard in browser
2. Select "Sales" from department dropdown
3. Click "Apply Filters" button
4. Verify table shows only Sales employees
5. Click "Reset" button
6. Observe employee table

### Expected Behavior
After clicking Reset, the employee table should display all employees from all departments.

### Actual Behavior
Employee table continues to show only Sales employees after reset.

### Root Cause
JavaScript `resetFilters()` function not properly clearing the filter state.

### Suggested Fix
Update `resetFilters()` function to properly reset dropdown values and repopulate table:
```javascript
function resetFilters() {
    document.getElementById('departmentFilter').value = 'all';
    document.getElementById('jobRoleFilter').value = 'all';
    populateEmployeeTable(employeeData);  // Use original data
    showNotification('Filters reset');
}
```

### Attachments
- Video recording of the issue
- Browser console output

---

## Bug Report #4 - Medium

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-004 |
| **Title** | API returns incorrect attrition rate for empty dataset |
| **Severity** | Medium |
| **Priority** | P2 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-18 |
| **Assigned To** | Backend Developer |
| **Environment** | Development |

### Description
When querying the `/attrition-stats` endpoint with a filter that returns no employees, the API returns an attrition rate of "NaN" instead of 0 or an appropriate error message.

### Steps to Reproduce
1. Start API server
2. Send GET request to `/employees?department=NonExistentDept`
3. Note the empty response
4. Send GET request to `/attrition-stats`
5. Observe attrition_rate value

### Expected Behavior
API should return:
- Attrition rate of 0 if no employees match filter
- Or appropriate error message for invalid filter

### Actual Behavior
API returns `attrition_rate: NaN` in the response.

### Root Cause
Division by zero not handled in attrition rate calculation.

### Suggested Fix
Add validation before division:
```python
attrition_rate = (attrition_count / total_employees) * 100 if total_employees > 0 else 0
```

### Attachments
- API response JSON showing NaN value
- Postman test results

---

## Bug Report #5 - Low

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-005 |
| **Title** | Typo in dashboard footer text |
| **Severity** | Low |
| **Priority** | P3 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-19 |
| **Assigned To** | Frontend Developer |
| **Environment** | Production |

### Description
The dashboard footer contains a typo: "Analsis" instead of "Analysis" in the copyright text.

### Steps to Reproduce
1. Open dashboard in browser
2. Scroll to footer section
3. Read the footer text

### Expected Behavior
Footer should read: "HR Employee Attrition Analysis Dashboard"

### Actual Behavior
Footer reads: "HR Employee Attrition Analsis Dashboard"

### Root Cause
Typo in HTML footer element.

### Suggested Fix
Correct the spelling in `dashboard/index.html`:
```html
<p class="text-sm">
    <i class="fas fa-chart-line mr-2"></i>
    HR Employee Attrition Analysis Dashboard | Built with HTML, Tailwind CSS & Chart.js
</p>
```

### Attachments
- Screenshot of footer with typo

---

## Bug Report #6 - Low

| Field | Details |
|-------|---------|
| **Bug ID** | BUG-006 |
| **Title** | Employee table shows scrollbar on desktop view |
| **Severity** | Low |
| **Priority** | P3 |
| **Status** | Open |
| **Reported By** | QA Engineer |
| **Reported Date** | 2024-01-20 |
| **Assigned To** | Frontend Developer |
| **Environment** | Development |

### Description
On desktop view (1920x1080), the employee table shows a horizontal scrollbar even though the table content fits within the container. This creates a poor user experience.

### Steps to Reproduce
1. Open dashboard on desktop browser (1920x1080 resolution)
2. Scroll to employee table section
3. Observe horizontal scrollbar

### Expected Behavior
Table should fit within the container without horizontal scrollbar on desktop view.

### Actual Behavior
Horizontal scrollbar appears on desktop view.

### Root Cause
Table width calculation or CSS overflow property not optimized for desktop.

### Suggested Fix
Adjust CSS for table container:
```css
.overflow-x-auto {
    overflow-x: auto;
}
@media (min-width: 1024px) {
    .overflow-x-auto {
        overflow-x: hidden;
    }
}
```

### Attachments
- Screenshot of table with scrollbar
- CSS inspection results

---

## Bug Summary Report

| Severity | Count | Percentage |
|----------|-------|------------|
| Critical | 1 | 16.7% |
| High | 1 | 16.7% |
| Medium | 2 | 33.3% |
| Low | 2 | 33.3% |
| **Total** | **6** | **100%** |

### Bug Status Distribution

| Status | Count |
|--------|-------|
| Open | 6 |
| In Progress | 0 |
| Resolved | 0 |
| Closed | 0 |

### Priority Distribution

| Priority | Count |
|----------|-------|
| P1 | 2 |
| P2 | 2 |
| P3 | 2 |

### Recommendations

1. **Immediate Action**: Fix BUG-001 (Critical) and BUG-002 (High) before release
2. **Short-term**: Address BUG-003 and BUG-004 in next sprint
3. **Long-term**: Fix cosmetic issues (BUG-005, BUG-006) when time permits
4. **Process Improvement**: Add input validation and error handling to prevent similar bugs
