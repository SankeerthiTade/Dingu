import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class EmployeePerformanceCalculator:
    def __init__(self, name, department, emp_id, tasks_assigned, tasks_completed, leaves_taken):
        self.name = name
        self.department = department
        self.emp_id = emp_id
        self.tasks_assigned = tasks_assigned
        self.tasks_completed = tasks_completed
        self.leaves_taken = leaves_taken

    def calculate_performance(self):
        task_status = "Exuberant" if self.tasks_completed == self.tasks_assigned else "Average" if self.tasks_completed >= self.tasks_assigned / 2 else "Poor"
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
        tasks_assigned = st.number_input("Number of Tasks Assigned:", min_value=0)
        tasks_completed = st.number_input("Number of Tasks Completed:", min_value=0, max_value=tasks_assigned)
        leaves_taken = st.number_input("Number of Leaves Taken:", min_value=0)

        employee = EmployeePerformanceCalculator(name, department, emp_id, tasks_assigned, tasks_completed, leaves_taken)
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
        overall_tasks_completed = sum(employee.tasks_completed for employee in employee_data)
        overall_leaves_taken = sum(employee.leaves_taken for employee in employee_data)

        # Display overall performance status
        st.subheader("Overall Performance Metrics")
        st.text(f"Overall Tasks Assigned: {overall_tasks_assigned}")
        st.text(f"Overall Tasks Completed: {overall_tasks_completed}")
        st.text(f"Overall Leaves Taken: {overall_leaves_taken}")

if __name__ == "__main__":
    main()
