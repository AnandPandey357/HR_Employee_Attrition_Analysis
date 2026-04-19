"""
HR Employee Attrition Analysis - Mock REST API Server
This Flask application provides REST API endpoints for the HR dashboard.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load employee data
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw', 'hr_employee_data.csv')

try:
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Loaded {len(df)} employee records from {DATA_PATH}")
except FileNotFoundError:
    print(f"⚠ Data file not found at {DATA_PATH}")
    df = pd.DataFrame()


@app.route('/', methods=['GET'])
def home():
    """API home endpoint"""
    return jsonify({
        'message': 'HR Employee Attrition Analysis API',
        'version': '1.0.0',
        'endpoints': {
            '/employees': 'GET - Get all employees',
            '/employees/<id>': 'GET - Get employee by ID',
            '/attrition-stats': 'GET - Get attrition statistics',
            '/kpi-metrics': 'GET - Get KPI metrics',
            '/department-stats': 'GET - Get statistics by department',
            '/salary-stats': 'GET - Get salary statistics'
        }
    })


@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Get all employees with optional filtering
    Query params: department, job_role, attrition
    """
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    # Get query parameters
    department = request.args.get('department')
    job_role = request.args.get('job_role')
    attrition = request.args.get('attrition')
    
    # Apply filters
    filtered_df = df.copy()
    
    if department:
        filtered_df = filtered_df[filtered_df['Department'] == department]
    
    if job_role:
        filtered_df = filtered_df[filtered_df['JobRole'] == job_role]
    
    if attrition:
        filtered_df = filtered_df[filtered_df['Attrition'] == attrition]
    
    # Convert to list of dictionaries
    employees = filtered_df.to_dict(orient='records')
    
    return jsonify({
        'total': len(employees),
        'data': employees
    })


@app.route('/employees/<employee_id>', methods=['GET'])
def get_employee_by_id(employee_id):
    """Get a specific employee by ID"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    employee = df[df['EmployeeID'] == employee_id]
    
    if employee.empty:
        return jsonify({'error': 'Employee not found'}), 404
    
    return jsonify(employee.to_dict(orient='records')[0])


@app.route('/attrition-stats', methods=['GET'])
def get_attrition_stats():
    """
    Get comprehensive attrition statistics
    Includes: overall rate, by department, by job role, by salary range
    """
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    total_employees = len(df)
    attrition_count = len(df[df['Attrition'] == 'Yes'])
    attrition_rate = (attrition_count / total_employees) * 100 if total_employees > 0 else 0
    
    # Attrition by department
    dept_stats = {}
    for dept in df['Department'].unique():
        dept_data = df[df['Department'] == dept]
        dept_attrition = len(dept_data[dept_data['Attrition'] == 'Yes'])
        dept_stats[dept] = {
            'total': len(dept_data),
            'attrition': dept_attrition,
            'attrition_rate': round((dept_attrition / len(dept_data)) * 100, 2) if len(dept_data) > 0 else 0
        }
    
    # Attrition by job role
    role_stats = {}
    for role in df['JobRole'].unique():
        role_data = df[df['JobRole'] == role]
        role_attrition = len(role_data[role_data['Attrition'] == 'Yes'])
        role_stats[role] = {
            'total': len(role_data),
            'attrition': role_attrition,
            'attrition_rate': round((role_attrition / len(role_data)) * 100, 2) if len(role_data) > 0 else 0
        }
    
    # Overtime impact
    overtime_yes = df[df['Overtime'] == 'Yes']
    overtime_no = df[df['Overtime'] == 'No']
    
    overtime_stats = {
        'with_overtime': {
            'total': len(overtime_yes),
            'attrition': len(overtime_yes[overtime_yes['Attrition'] == 'Yes']),
            'attrition_rate': round((len(overtime_yes[overtime_yes['Attrition'] == 'Yes']) / len(overtime_yes)) * 100, 2) if len(overtime_yes) > 0 else 0
        },
        'without_overtime': {
            'total': len(overtime_no),
            'attrition': len(overtime_no[overtime_no['Attrition'] == 'Yes']),
            'attrition_rate': round((len(overtime_no[overtime_no['Attrition'] == 'Yes']) / len(overtime_no)) * 100, 2) if len(overtime_no) > 0 else 0
        }
    }
    
    return jsonify({
        'overall': {
            'total_employees': total_employees,
            'attrition_count': attrition_count,
            'attrition_rate': round(attrition_rate, 2)
        },
        'by_department': dept_stats,
        'by_job_role': role_stats,
        'overtime_impact': overtime_stats
    })


@app.route('/kpi-metrics', methods=['GET'])
def get_kpi_metrics():
    """Get key performance indicators"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    total_employees = len(df)
    attrition_count = len(df[df['Attrition'] == 'Yes'])
    attrition_rate = (attrition_count / total_employees) * 100 if total_employees > 0 else 0
    avg_salary = df['MonthlyIncome'].mean()
    avg_age = df['Age'].mean()
    avg_job_satisfaction = df['JobSatisfaction'].mean()
    avg_work_life_balance = df['WorkLifeBalance'].mean()
    
    return jsonify({
        'total_employees': int(total_employees),
        'attrition_count': int(attrition_count),
        'attrition_rate': round(attrition_rate, 2),
        'average_salary': round(avg_salary, 2),
        'average_age': round(avg_age, 2),
        'average_job_satisfaction': round(avg_job_satisfaction, 2),
        'average_work_life_balance': round(avg_work_life_balance, 2)
    })


@app.route('/department-stats', methods=['GET'])
def get_department_stats():
    """Get statistics by department"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    dept_stats = {}
    for dept in df['Department'].unique():
        dept_data = df[df['Department'] == dept]
        dept_stats[dept] = {
            'total_employees': int(len(dept_data)),
            'average_salary': round(dept_data['MonthlyIncome'].mean(), 2),
            'average_age': round(dept_data['Age'].mean(), 2),
            'attrition_count': int(len(dept_data[dept_data['Attrition'] == 'Yes'])),
            'attrition_rate': round((len(dept_data[dept_data['Attrition'] == 'Yes']) / len(dept_data)) * 100, 2) if len(dept_data) > 0 else 0,
            'job_roles': list(dept_data['JobRole'].unique())
        }
    
    return jsonify(dept_stats)


@app.route('/salary-stats', methods=['GET'])
def get_salary_stats():
    """Get salary statistics and distribution"""
    if df.empty:
        return jsonify({'error': 'No data available'}), 404
    
    # Salary quartiles
    salary_q1 = df['MonthlyIncome'].quantile(0.25)
    salary_median = df['MonthlyIncome'].median()
    salary_q3 = df['MonthlyIncome'].quantile(0.75)
    
    # Salary ranges
    salary_ranges = {
        'low': {
            'range': '< $4000',
            'count': int(len(df[df['MonthlyIncome'] < 4000])),
            'attrition_rate': round((len(df[df['MonthlyIncome'] < 4000][df['Attrition'] == 'Yes']) / len(df[df['MonthlyIncome'] < 4000])) * 100, 2) if len(df[df['MonthlyIncome'] < 4000]) > 0 else 0
        },
        'medium_low': {
            'range': '$4000 - $6000',
            'count': int(len(df[(df['MonthlyIncome'] >= 4000) & (df['MonthlyIncome'] < 6000)])),
            'attrition_rate': round((len(df[(df['MonthlyIncome'] >= 4000) & (df['MonthlyIncome'] < 6000)][df['Attrition'] == 'Yes']) / len(df[(df['MonthlyIncome'] >= 4000) & (df['MonthlyIncome'] < 6000)])) * 100, 2) if len(df[(df['MonthlyIncome'] >= 4000) & (df['MonthlyIncome'] < 6000)]) > 0 else 0
        },
        'medium_high': {
            'range': '$6000 - $8000',
            'count': int(len(df[(df['MonthlyIncome'] >= 6000) & (df['MonthlyIncome'] < 8000)])),
            'attrition_rate': round((len(df[(df['MonthlyIncome'] >= 6000) & (df['MonthlyIncome'] < 8000)][df['Attrition'] == 'Yes']) / len(df[(df['MonthlyIncome'] >= 6000) & (df['MonthlyIncome'] < 8000)])) * 100, 2) if len(df[(df['MonthlyIncome'] >= 6000) & (df['MonthlyIncome'] < 8000)]) > 0 else 0
        },
        'high': {
            'range': '> $8000',
            'count': int(len(df[df['MonthlyIncome'] >= 8000])),
            'attrition_rate': round((len(df[df['MonthlyIncome'] >= 8000][df['Attrition'] == 'Yes']) / len(df[df['MonthlyIncome'] >= 8000])) * 100, 2) if len(df[df['MonthlyIncome'] >= 8000]) > 0 else 0
        }
    }
    
    # Salary by attrition status
    salary_by_attrition = {
        'attrition_yes': {
            'average': round(df[df['Attrition'] == 'Yes']['MonthlyIncome'].mean(), 2),
            'min': float(df[df['Attrition'] == 'Yes']['MonthlyIncome'].min()),
            'max': float(df[df['Attrition'] == 'Yes']['MonthlyIncome'].max())
        },
        'attrition_no': {
            'average': round(df[df['Attrition'] == 'No']['MonthlyIncome'].mean(), 2),
            'min': float(df[df['Attrition'] == 'No']['MonthlyIncome'].min()),
            'max': float(df[df['Attrition'] == 'No']['MonthlyIncome'].max())
        }
    }
    
    return jsonify({
        'overall_stats': {
            'mean': round(df['MonthlyIncome'].mean(), 2),
            'median': round(salary_median, 2),
            'min': float(df['MonthlyIncome'].min()),
            'max': float(df['MonthlyIncome'].max()),
            'std': round(df['MonthlyIncome'].std(), 2)
        },
        'quartiles': {
            'q1': round(salary_q1, 2),
            'median': round(salary_median, 2),
            'q3': round(salary_q3, 2)
        },
        'by_range': salary_ranges,
        'by_attrition': salary_by_attrition
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    print("=" * 60)
    print("HR EMPLOYEE ATTRITION ANALYSIS API SERVER")
    print("=" * 60)
    print("\nAvailable Endpoints:")
    print("  GET  /                    - API information")
    print("  GET  /employees           - Get all employees")
    print("  GET  /employees/<id>      - Get employee by ID")
    print("  GET  /attrition-stats     - Get attrition statistics")
    print("  GET  /kpi-metrics         - Get KPI metrics")
    print("  GET  /department-stats    - Get department statistics")
    print("  GET  /salary-stats        - Get salary statistics")
    print("\nServer starting on http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
