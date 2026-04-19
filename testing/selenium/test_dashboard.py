"""
HR Employee Attrition Dashboard - Selenium Automation Tests
This script automates UI testing for the HR dashboard using Selenium WebDriver.
Language: Python
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pytest
import os


class TestHRDashboard:
    """Test class for HR Dashboard UI automation"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup and teardown for each test"""
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        
        # Get the dashboard file path
        dashboard_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', '..', 'dashboard', 'index.html'
        ))
        self.dashboard_url = f'file:///{dashboard_path}'
        
        yield
        
        # Cleanup
        self.driver.quit()
    
    def test_dashboard_loading(self):
        """Test 1: Verify dashboard loads correctly"""
        print("\n=== Test 1: Dashboard Loading ===")
        
        # Navigate to dashboard
        self.driver.get(self.dashboard_url)
        
        # Verify page title
        assert "HR Employee Attrition" in self.driver.title, "Page title incorrect"
        print("✓ Page title verified")
        
        # Verify header is present
        header = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "header"))
        )
        assert header.is_displayed(), "Header not displayed"
        print("✓ Header is displayed")
        
        # Verify dashboard heading
        heading = self.driver.find_element(By.XPATH, "//h1[contains(text(), 'HR Employee Attrition')]")
        assert heading.is_displayed(), "Dashboard heading not found"
        print("✓ Dashboard heading verified")
        
        print("✓ Test 1 PASSED: Dashboard loads correctly")
    
    def test_kpi_cards_display(self):
        """Test 2: Verify KPI cards are displayed with correct data"""
        print("\n=== Test 2: KPI Cards Display ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)  # Wait for JavaScript to load data
        
        # Verify Total Employees card
        total_employees = self.driver.find_element(By.ID, "totalEmployees")
        assert total_employees.is_displayed(), "Total Employees card not displayed"
        assert total_employees.text != "0", "Total Employees should not be 0"
        print(f"✓ Total Employees: {total_employees.text}")
        
        # Verify Attrition Rate card
        attrition_rate = self.driver.find_element(By.ID, "attritionRate")
        assert attrition_rate.is_displayed(), "Attrition Rate card not displayed"
        assert "%" in attrition_rate.text, "Attrition Rate should contain %"
        print(f"✓ Attrition Rate: {attrition_rate.text}")
        
        # Verify Average Salary card
        avg_salary = self.driver.find_element(By.ID, "avgSalary")
        assert avg_salary.is_displayed(), "Average Salary card not displayed"
        assert "$" in avg_salary.text, "Average Salary should contain $"
        print(f"✓ Average Salary: {avg_salary.text}")
        
        # Verify Average Satisfaction card
        avg_satisfaction = self.driver.find_element(By.ID, "avgSatisfaction")
        assert avg_satisfaction.is_displayed(), "Average Satisfaction card not displayed"
        print(f"✓ Average Satisfaction: {avg_satisfaction.text}")
        
        print("✓ Test 2 PASSED: All KPI cards displayed correctly")
    
    def test_charts_rendering(self):
        """Test 3: Verify all charts are rendered"""
        print("\n=== Test 3: Charts Rendering ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(3)  # Wait for charts to render
        
        # List of chart canvas elements
        charts = [
            ("Department Chart", "departmentChart"),
            ("Salary Chart", "salaryChart"),
            ("Overtime Chart", "overtimeChart"),
            ("Satisfaction Chart", "satisfactionChart")
        ]
        
        for chart_name, chart_id in charts:
            try:
                chart = self.driver.find_element(By.ID, chart_id)
                assert chart.is_displayed(), f"{chart_name} not displayed"
                print(f"✓ {chart_name} is rendered")
            except Exception as e:
                print(f"✗ {chart_name} failed to render: {e}")
                raise
        
        print("✓ Test 3 PASSED: All charts rendered successfully")
    
    def test_filter_functionality(self):
        """Test 4: Verify filter functionality works correctly"""
        print("\n=== Test 4: Filter Functionality ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)
        
        # Get initial employee count
        table_body = self.driver.find_element(By.ID, "employeeTableBody")
        initial_rows = len(table_body.find_elements(By.TAG_NAME, "tr"))
        print(f"Initial employee count: {initial_rows}")
        
        # Select department filter
        dept_filter = self.driver.find_element(By.ID, "departmentFilter")
        dept_filter.send_keys("Sales")
        
        # Apply filters
        apply_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filters')]")
        apply_button.click()
        time.sleep(2)
        
        # Verify filtered results
        table_body = self.driver.find_element(By.ID, "employeeTableBody")
        filtered_rows = len(table_body.find_elements(By.TAG_NAME, "tr"))
        print(f"Filtered employee count (Sales): {filtered_rows}")
        
        # Verify all rows are from Sales department
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) > 3:
                assert "Sales" in cells[3].text, f"Non-Sales employee found: {cells[3].text}"
        
        print("✓ Department filter works correctly")
        
        # Reset filters
        reset_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Reset')]")
        reset_button.click()
        time.sleep(2)
        
        # Verify reset worked
        table_body = self.driver.find_element(By.ID, "employeeTableBody")
        reset_rows = len(table_body.find_elements(By.TAG_NAME, "tr"))
        assert reset_rows == initial_rows, "Reset did not restore original data"
        print(f"✓ Reset restored original count: {reset_rows}")
        
        print("✓ Test 4 PASSED: Filter functionality works correctly")
    
    def test_insights_section(self):
        """Test 5: Verify insights section is populated"""
        print("\n=== Test 5: Insights Section ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)
        
        # Verify insights container exists
        insights_container = self.driver.find_element(By.ID, "insightsContainer")
        assert insights_container.is_displayed(), "Insights container not displayed"
        print("✓ Insights container is displayed")
        
        # Verify insights are populated
        insight_cards = insights_container.find_elements(By.CLASS_NAME, "bg-gray-50")
        assert len(insight_cards) > 0, "No insight cards found"
        print(f"✓ Found {len(insight_cards)} insight cards")
        
        # Verify each insight has title and text
        for card in insight_cards:
            assert card.is_displayed(), "Insight card not displayed"
            text = card.text
            assert len(text) > 0, "Insight card has no text"
        
        print("✓ Test 5 PASSED: Insights section populated correctly")
    
    def test_employee_table_data(self):
        """Test 6: Verify employee table contains valid data"""
        print("\n=== Test 6: Employee Table Data ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)
        
        # Get table body
        table_body = self.driver.find_element(By.ID, "employeeTableBody")
        rows = table_body.find_elements(By.TAG_NAME, "tr")
        
        assert len(rows) > 0, "Employee table is empty"
        print(f"✓ Table contains {len(rows)} rows")
        
        # Verify first row has correct columns
        first_row = rows[0]
        cells = first_row.find_elements(By.TAG_NAME, "td")
        
        expected_columns = 9  # Employee ID, Age, Gender, Department, Job Role, Salary, Satisfaction, Overtime, Attrition
        assert len(cells) == expected_columns, f"Expected {expected_columns} columns, got {len(cells)}"
        print(f"✓ Table has {expected_columns} columns")
        
        # Verify Employee ID format
        emp_id = cells[0].text
        assert emp_id.startswith("EMP"), f"Invalid Employee ID format: {emp_id}"
        print(f"✓ Employee ID format valid: {emp_id}")
        
        # Verify Age is a number
        age = cells[1].text
        assert age.isdigit(), f"Age should be a number: {age}"
        print(f"✓ Age is valid: {age}")
        
        # Verify Attrition badge exists
        attrition_cell = cells[8]
        assert attrition_cell.is_displayed(), "Attrition cell not displayed"
        print("✓ Attrition status displayed")
        
        print("✓ Test 6 PASSED: Employee table data is valid")
    
    def test_responsive_design(self):
        """Test 7: Verify dashboard is responsive"""
        print("\n=== Test 7: Responsive Design ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)
        
        # Test different screen sizes
        screen_sizes = [
            (1920, 1080, "Desktop"),
            (768, 1024, "Tablet"),
            (375, 667, "Mobile")
        ]
        
        for width, height, device in screen_sizes:
            self.driver.set_window_size(width, height)
            time.sleep(1)
            
            # Verify header is still visible
            header = self.driver.find_element(By.TAG_NAME, "header")
            assert header.is_displayed(), f"Header not visible on {device}"
            
            # Verify KPI cards are visible
            total_employees = self.driver.find_element(By.ID, "totalEmployees")
            assert total_employees.is_displayed(), f"KPI cards not visible on {device}"
            
            print(f"✓ Dashboard responsive on {device} ({width}x{height})")
        
        # Reset to desktop size
        self.driver.set_window_size(1920, 1080)
        
        print("✓ Test 7 PASSED: Dashboard is responsive")
    
    def test_ui_elements_interactivity(self):
        """Test 8: Verify UI elements are interactive"""
        print("\n=== Test 8: UI Elements Interactivity ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)
        
        # Test dropdown interactivity
        dept_filter = self.driver.find_element(By.ID, "departmentFilter")
        dept_filter.click()
        assert dept_filter.is_enabled(), "Department filter not enabled"
        print("✓ Department filter is clickable")
        
        # Test button interactivity
        apply_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Apply Filters')]")
        assert apply_button.is_enabled(), "Apply button not enabled"
        print("✓ Apply button is clickable")
        
        reset_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Reset')]")
        assert reset_button.is_enabled(), "Reset button not enabled"
        print("✓ Reset button is clickable")
        
        print("✓ Test 8 PASSED: UI elements are interactive")
    
    def test_last_updated_timestamp(self):
        """Test 9: Verify last updated timestamp is displayed"""
        print("\n=== Test 9: Last Updated Timestamp ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(2)
        
        # Verify last updated element exists
        last_updated = self.driver.find_element(By.ID, "lastUpdated")
        assert last_updated.is_displayed(), "Last updated timestamp not displayed"
        
        # Verify timestamp has content
        timestamp = last_updated.text
        assert len(timestamp) > 0, "Timestamp is empty"
        print(f"✓ Last updated: {timestamp}")
        
        print("✓ Test 9 PASSED: Last updated timestamp displayed")
    
    def test_footer_elements(self):
        """Test 10: Verify footer elements are present"""
        print("\n=== Test 10: Footer Elements ===")
        
        self.driver.get(self.dashboard_url)
        time.sleep(1)
        
        # Verify footer exists
        footer = self.driver.find_element(By.TAG_NAME, "footer")
        assert footer.is_displayed(), "Footer not displayed"
        print("✓ Footer is displayed")
        
        # Verify footer contains expected text
        footer_text = footer.text
        assert "HR Employee Attrition" in footer_text, "Footer missing expected text"
        print("✓ Footer contains expected text")
        
        print("✓ Test 10 PASSED: Footer elements verified")


def run_tests():
    """Run all tests and generate report"""
    print("=" * 60)
    print("HR DASHBOARD SELENIUM AUTOMATION TESTS")
    print("=" * 60)
    
    # Run pytest
    exit_code = pytest.main([
        __file__,
        '-v',
        '--html=../output/test_report.html',
        '--self-contained-html'
    ])
    
    print("\n" + "=" * 60)
    if exit_code == 0:
        print("ALL TESTS PASSED ✓")
    else:
        print("SOME TESTS FAILED ✗")
    print("=" * 60)
    
    return exit_code


if __name__ == "__main__":
    run_tests()
