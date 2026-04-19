// HR Employee Attrition Dashboard - JavaScript

// Mock data for dashboard (simulating API response)
const dashboardData = {
    kpi_metrics: {
        total_employees: 20,
        attrition_count: 7,
        attrition_rate: 35.00,
        average_salary: 6265.00,
        avg_age: 36.45,
        avg_job_satisfaction: 3.15,
        avg_work_life_balance: 2.55
    },
    attrition_by_department: {
        "Sales": { total: 8, attrition: 4, attrition_rate: 50.00 },
        "Research & Development": { total: 8, attrition: 2, attrition_rate: 25.00 },
        "Human Resources": { total: 4, attrition: 1, attrition_rate: 25.00 }
    },
    attrition_by_salary_range: {
        "<4000": { total: 4, attrition: 3, attrition_rate: 75.00 },
        "4000-6000": { total: 7, attrition: 2, attrition_rate: 28.57 },
        "6000-8000": { total: 4, attrition: 1, attrition_rate: 25.00 },
        ">8000": { total: 5, attrition: 1, attrition_rate: 20.00 }
    },
    overtime_impact: {
        "Yes": { total: 9, attrition: 5, attrition_rate: 55.56 },
        "No": { total: 11, attrition: 2, attrition_rate: 18.18 }
    },
    job_role_distribution: {
        "Sales Executive": { count: 4, avg_salary: 4375, attrition_rate: 50.00 },
        "Sales Representative": { count: 3, avg_salary: 3733, attrition_rate: 66.67 },
        "Research Scientist": { count: 3, avg_salary: 6500, attrition_rate: 0.00 },
        "Laboratory Technician": { count: 3, avg_salary: 5000, attrition_rate: 33.33 },
        "HR Manager": { count: 2, avg_salary: 8350, attrition_rate: 0.00 },
        "HR Specialist": { count: 2, avg_salary: 4350, attrition_rate: 50.00 },
        "Sales Manager": { count: 1, avg_salary: 9500, attrition_rate: 0.00 },
        "Research Director": { count: 2, avg_salary: 11750, attrition_rate: 0.00 }
    }
};

// Employee data for table
const employeeData = [
    { id: "EMP001", age: 32, gender: "Male", dept: "Sales", role: "Sales Executive", salary: 4500, satisfaction: 3, overtime: "Yes", attrition: "Yes" },
    { id: "EMP002", age: 41, gender: "Female", dept: "Research & Development", role: "Research Scientist", salary: 6500, satisfaction: 4, overtime: "No", attrition: "No" },
    { id: "EMP003", age: 28, gender: "Male", dept: "Sales", role: "Sales Representative", salary: 3500, satisfaction: 2, overtime: "Yes", attrition: "Yes" },
    { id: "EMP004", age: 45, gender: "Female", dept: "Research & Development", role: "Laboratory Technician", salary: 5000, satisfaction: 3, overtime: "No", attrition: "No" },
    { id: "EMP005", age: 36, gender: "Male", dept: "Human Resources", role: "HR Manager", salary: 8500, satisfaction: 4, overtime: "No", attrition: "No" },
    { id: "EMP006", age: 29, gender: "Female", dept: "Sales", role: "Sales Executive", salary: 4200, satisfaction: 2, overtime: "Yes", attrition: "Yes" },
    { id: "EMP007", age: 52, gender: "Male", dept: "Research & Development", role: "Research Director", salary: 12000, satisfaction: 5, overtime: "No", attrition: "No" },
    { id: "EMP008", age: 31, gender: "Female", dept: "Sales", role: "Sales Representative", salary: 3800, satisfaction: 3, overtime: "Yes", attrition: "No" },
    { id: "EMP009", age: 38, gender: "Male", dept: "Research & Development", role: "Research Scientist", salary: 6200, satisfaction: 3, overtime: "No", attrition: "No" },
    { id: "EMP010", age: 27, gender: "Female", dept: "Human Resources", role: "HR Specialist", salary: 4500, satisfaction: 2, overtime: "Yes", attrition: "Yes" }
];

// Business insights
const businessInsights = [
    {
        title: "Overtime Impact",
        icon: "fas fa-clock",
        color: "orange",
        text: "Employees working overtime have 55.6% attrition rate vs 18.2% for those without. Excessive workload is a key driver of turnover."
    },
    {
        title: "Salary Correlation",
        icon: "fas fa-dollar-sign",
        color: "green",
        text: "Low salary employees (<$4000) have 75% attrition rate. Competitive compensation is critical for retention."
    },
    {
        title: "Department Risk",
        icon: "fas fa-building",
        color: "blue",
        text: "Sales department has highest attrition (50%). Investigate department-specific issues like targets and pressure."
    },
    {
        title: "Job Satisfaction",
        icon: "fas fa-smile",
        color: "purple",
        text: "Low satisfaction scores correlate with higher attrition. Regular surveys and feedback mechanisms are essential."
    },
    {
        title: "Work-Life Balance",
        icon: "fas fa-balance-scale",
        color: "indigo",
        text: "Poor work-life balance ratings show 2x higher attrition. Flexible work arrangements can improve retention."
    },
    {
        title: "Action Required",
        icon: "fas fa-exclamation-circle",
        color: "red",
        text: "Immediate intervention needed for employees with overtime + low satisfaction + below-average salary."
    }
];

// Initialize dashboard
document.addEventListener('DOMContentLoaded', function() {
    updateLastUpdated();
    updateKPICards();
    initializeCharts();
    populateInsights();
    populateEmployeeTable();
});

// Update last updated timestamp
function updateLastUpdated() {
    const now = new Date();
    document.getElementById('lastUpdated').textContent = now.toLocaleString();
}

// Update KPI cards
function updateKPICards() {
    document.getElementById('totalEmployees').textContent = dashboardData.kpi_metrics.total_employees;
    document.getElementById('attritionRate').textContent = dashboardData.kpi_metrics.attrition_rate + '%';
    document.getElementById('avgSalary').textContent = '$' + dashboardData.kpi_metrics.average_salary.toLocaleString();
    document.getElementById('avgSatisfaction').textContent = dashboardData.kpi_metrics.avg_job_satisfaction.toFixed(1);
}

// Initialize all charts
function initializeCharts() {
    createDepartmentChart();
    createSalaryChart();
    createOvertimeChart();
    createSatisfactionChart();
}

// Department Attrition Chart
function createDepartmentChart() {
    const ctx = document.getElementById('departmentChart').getContext('2d');
    const departments = Object.keys(dashboardData.attrition_by_department);
    const attritionRates = departments.map(dept => 
        dashboardData.attrition_by_department[dept].attrition_rate
    );
    const totalEmployees = departments.map(dept => 
        dashboardData.attrition_by_department[dept].total
    );

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: departments,
            datasets: [{
                label: 'Attrition Rate (%)',
                data: attritionRates,
                backgroundColor: [
                    'rgba(239, 68, 68, 0.8)',
                    'rgba(59, 130, 246, 0.8)',
                    'rgba(59, 130, 246, 0.8)'
                ],
                borderColor: [
                    'rgb(239, 68, 68)',
                    'rgb(59, 130, 246)',
                    'rgb(59, 130, 246)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });
}

// Salary vs Attrition Chart
function createSalaryChart() {
    const ctx = document.getElementById('salaryChart').getContext('2d');
    const salaryRanges = Object.keys(dashboardData.attrition_by_salary_range);
    const attritionRates = salaryRanges.map(range => 
        dashboardData.attrition_by_salary_range[range].attrition_rate
    );

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: salaryRanges,
            datasets: [{
                label: 'Attrition Rate (%)',
                data: attritionRates,
                fill: true,
                backgroundColor: 'rgba(16, 185, 129, 0.2)',
                borderColor: 'rgb(16, 185, 129)',
                tension: 0.4,
                pointBackgroundColor: 'rgb(16, 185, 129)',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 6
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        callback: function(value) {
                            return value + '%';
                        }
                    }
                }
            }
        }
    });
}

// Overtime Impact Chart
function createOvertimeChart() {
    const ctx = document.getElementById('overtimeChart').getContext('2d');
    const overtimeStatus = Object.keys(dashboardData.overtime_impact);
    const attritionRates = overtimeStatus.map(status => 
        dashboardData.overtime_impact[status].attrition_rate
    );

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['With Overtime', 'Without Overtime'],
            datasets: [{
                data: attritionRates,
                backgroundColor: [
                    'rgba(249, 115, 22, 0.8)',
                    'rgba(34, 197, 94, 0.8)'
                ],
                borderColor: [
                    'rgb(249, 115, 22)',
                    'rgb(34, 197, 94)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return context.label + ': ' + context.raw + '%';
                        }
                    }
                }
            }
        }
    });
}

// Job Satisfaction Distribution Chart
function createSatisfactionChart() {
    const ctx = document.getElementById('satisfactionChart').getContext('2d');
    
    // Calculate satisfaction distribution
    const satisfactionLevels = [1, 2, 3, 4, 5];
    const satisfactionCounts = satisfactionLevels.map(level => {
        return employeeData.filter(emp => emp.satisfaction === level).length;
    });

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'],
            datasets: [{
                label: 'Number of Employees',
                data: satisfactionCounts,
                backgroundColor: [
                    'rgba(239, 68, 68, 0.8)',
                    'rgba(249, 115, 22, 0.8)',
                    'rgba(234, 179, 8, 0.8)',
                    'rgba(34, 197, 94, 0.8)',
                    'rgba(16, 185, 129, 0.8)'
                ],
                borderColor: [
                    'rgb(239, 68, 68)',
                    'rgb(249, 115, 22)',
                    'rgb(234, 179, 8)',
                    'rgb(34, 197, 94)',
                    'rgb(16, 185, 129)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        stepSize: 1
                    }
                }
            }
        }
    });
}

// Populate insights section
function populateInsights() {
    const container = document.getElementById('insightsContainer');
    container.innerHTML = '';
    
    businessInsights.forEach(insight => {
        const card = document.createElement('div');
        card.className = 'bg-gray-50 rounded-lg p-4 border-l-4 border-' + insight.color + '-500';
        card.innerHTML = `
            <div class="flex items-start space-x-3">
                <div class="bg-${insight.color}-100 p-2 rounded-full">
                    <i class="${insight.icon} text-${insight.color}-600"></i>
                </div>
                <div>
                    <h4 class="font-semibold text-gray-800">${insight.title}</h4>
                    <p class="text-sm text-gray-600 mt-1">${insight.text}</p>
                </div>
            </div>
        `;
        container.appendChild(card);
    });
}

// Populate employee table
function populateEmployeeTable(filteredData = employeeData) {
    const tbody = document.getElementById('employeeTableBody');
    tbody.innerHTML = '';
    
    filteredData.forEach(emp => {
        const row = document.createElement('tr');
        row.className = 'border-b hover:bg-gray-50';
        
        const attritionClass = emp.attrition === 'Yes' ? 'text-red-600 font-semibold' : 'text-green-600';
        const attritionBadge = emp.attrition === 'Yes' 
            ? '<span class="bg-red-100 text-red-800 px-2 py-1 rounded-full text-xs">Yes</span>'
            : '<span class="bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs">No</span>';
        
        row.innerHTML = `
            <td class="px-4 py-3 font-medium">${emp.id}</td>
            <td class="px-4 py-3">${emp.age}</td>
            <td class="px-4 py-3">${emp.gender}</td>
            <td class="px-4 py-3">${emp.dept}</td>
            <td class="px-4 py-3">${emp.role}</td>
            <td class="px-4 py-3">$${emp.salary.toLocaleString()}</td>
            <td class="px-4 py-3">
                <div class="flex items-center">
                    <div class="w-16 bg-gray-200 rounded-full h-2 mr-2">
                        <div class="bg-purple-600 h-2 rounded-full" style="width: ${(emp.satisfaction / 5) * 100}%"></div>
                    </div>
                    <span class="text-sm">${emp.satisfaction}/5</span>
                </div>
            </td>
            <td class="px-4 py-3">
                <span class="px-2 py-1 rounded-full text-xs ${emp.overtime === 'Yes' ? 'bg-orange-100 text-orange-800' : 'bg-gray-100 text-gray-800'}">
                    ${emp.overtime}
                </span>
            </td>
            <td class="px-4 py-3">${attritionBadge}</td>
        `;
        tbody.appendChild(row);
    });
}

// Apply filters
function applyFilters() {
    const departmentFilter = document.getElementById('departmentFilter').value;
    const jobRoleFilter = document.getElementById('jobRoleFilter').value;
    
    let filteredData = [...employeeData];
    
    if (departmentFilter !== 'all') {
        filteredData = filteredData.filter(emp => emp.dept === departmentFilter);
    }
    
    if (jobRoleFilter !== 'all') {
        filteredData = filteredData.filter(emp => emp.role === jobRoleFilter);
    }
    
    populateEmployeeTable(filteredData);
    
    // Show filter applied notification
    showNotification('Filters applied successfully');
}

// Reset filters
function resetFilters() {
    document.getElementById('departmentFilter').value = 'all';
    document.getElementById('jobRoleFilter').value = 'all';
    populateEmployeeTable(employeeData);
    showNotification('Filters reset');
}

// Show notification
function showNotification(message) {
    const notification = document.createElement('div');
    notification.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50';
    notification.innerHTML = `<i class="fas fa-check-circle mr-2"></i>${message}`;
    document.body.appendChild(notification);
    
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Simulate API call to fetch data (for demonstration)
async function fetchDashboardData() {
    try {
        // In a real application, this would be an actual API call
        // const response = await fetch('/api/attrition-stats');
        // const data = await response.json();
        
        // For now, return mock data
        return dashboardData;
    } catch (error) {
        console.error('Error fetching dashboard data:', error);
        return null;
    }
}
