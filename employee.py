import streamlit as st
import pandas as pd

class EmployeePerformanceCalculator:
    def __init__(self, name, department, emp_id, project_name, start_date, end_date, tasks_assigned, tasks_pending, leaves_taken, attendance_monthly, attendance_daily):
        self.name = name
        self.department = department
        self.emp_id = emp_id
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks_assigned = tasks_assigned
        self.tasks_pending = tasks_pending
        self.leaves_taken = leaves_taken
        self.attendance_monthly = attendance_monthly
        self.attendance_daily = attendance_daily

    def calculate_performance(self):
        task_status = "Exuberant" if self.tasks_pending == 0 else "Average" if self.tasks_pending <= self.tasks_assigned / 2 else "Poor"
        leave_status = "Excellent" if self.leaves_taken == 0 else "Fair" if self.leaves_taken <= 2 else "Unfair"

        return task_status, leave_status

def main():
    st.title("Employee Performance Calculator")

    # Data storage
    employee_data = []

    # Function to add a new employee
    def add_employee():
        name = st.text_input("Name:")
        department = st.text_input("Department:")
        emp_id = st.text_input("Employee ID:")
        project_name = st.text_input("Project Name:")
        start_date = st.date_input("Project Starting Date:")
        end_date = st.date_input("Project Ending Date:")
        tasks_assigned = st.number_input("Number of Tasks Assigned:", min_value=0)
        tasks_pending = st.number_input("Number of Tasks Pending:", min_value=0, max_value=tasks_assigned)
        leaves_taken = st.number_input("Number of Leaves Taken:", min_value=0)
        attendance_monthly = st.number_input("Attendance for the Month (%):", min_value=0, max_value=100)
        attendance_daily = st.number_input("Daily Attendance (%):", min_value=0, max_value=100)

        employee = EmployeePerformanceCalculator(name, department, emp_id, project_name, start_date, end_date, tasks_assigned, tasks_pending, leaves_taken, attendance_monthly, attendance_daily)
        employee_data.append(employee)

    # Button to add a new employee
    if st.button("Add Employee"):
        add_employee()

    # Display details as a table
    if employee_data:
        st.subheader("Employee Details")
        df = pd.DataFrame([vars(employee) for employee in employee_data])
        st.table(df)

        # Calculate overall performance metrics for all employees
        overall_tasks_assigned = sum(employee.tasks_assigned for employee in employee_data)
        overall_tasks_pending = sum(employee.tasks_pending for employee in employee_data)
        overall_leaves_taken = sum(employee.leaves_taken for employee in employee_data)

        # Display overall performance status
        st.subheader("Overall Performance Metrics")
        st.text(f"Overall Tasks Assigned: {overall_tasks_assigned}")
        st.text(f"Overall Tasks Pending: {overall_tasks_pending}")
        st.text(f"Overall Leaves Taken: {overall_leaves_taken}")

if __name__ == "__main__":
    main()
