import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class EmployeePerformanceCalculator:
    def __init__(self, name, department, emp_id, tasks_assigned, tasks_completed, leaves_taken, attendance_percentage):
        self.name = name
        self.department = department
        self.emp_id = emp_id
        self.tasks_assigned = tasks_assigned
        self.tasks_completed = tasks_completed
        self.leaves_taken = leaves_taken
        self.attendance_percentage = attendance_percentage

    def calculate_performance(self):
        task_status = "Exuberant" if self.tasks_completed == self.tasks_assigned else "Average" if self.tasks_completed >= self.tasks_assigned / 2 else "Poor"
        leave_status = "Excellent" if self.leaves_taken == 0 else "Fair" if self.leaves_taken <= 2 else "Unfair"
        attendance_status = "Good" if self.attendance_percentage >= 90 else "Average" if self.attendance_percentage >= 80 else "Poor"

        return task_status, leave_status, attendance_status

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
        attendance_percentage = st.number_input("Attendance Percentage:", min_value=0, max_value=100)

        employee = EmployeePerformanceCalculator(name, department, emp_id, tasks_assigned, tasks_completed, leaves_taken, attendance_percentage)
        employee_data.append(employee)

    # Button to add a new employee
    if st.button("Add Employee"):
        add_employee()

    # Display details as a table and lollipop charts
    if employee_data:
        st.subheader("Employee Details")
        df = pd.DataFrame([vars(employee) for employee in employee_data])
        st.table(df)

        # Calculate overall performance metrics for all employees
        overall_tasks_assigned = sum(employee.tasks_assigned for employee in employee_data)
        overall_tasks_completed = sum(employee.tasks_completed for employee in employee_data)
        overall_leaves_taken = sum(employee.leaves_taken for employee in employee_data)
        overall_attendance_percentage = np.mean([employee.attendance_percentage for employee in employee_data])

        # Display overall performance status
        st.subheader("Overall Performance Metrics")
        st.text(f"Overall Tasks Assigned: {overall_tasks_assigned}")
        st.text(f"Overall Tasks Completed: {overall_tasks_completed}")
        st.text(f"Overall Leaves Taken: {overall_leaves_taken}")
        st.text(f"Overall Attendance Percentage: {overall_attendance_percentage:.2f}%")

        # Lollipop chart for overall performance metrics
        metrics_labels = ["Tasks Assigned", "Tasks Completed", "Leaves Taken", "Attendance Percentage"]
        metrics_values = [overall_tasks_assigned, overall_tasks_completed, overall_leaves_taken, overall_attendance_percentage]

        fig, ax = plt.subplots()
        ax.stem(metrics_labels, metrics_values, basefmt=" ", use_line_collection=True)
        ax.set_title("Overall Performance Metrics")
        ax.set_ylabel("Count/Percentage")

        # Display the lollipop chart
        st.write(fig)

if __name__ == "__main__":
    main()
