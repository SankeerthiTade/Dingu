import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

class EmployeePerformanceCalculator:
    def __init__(self, name, department, emp_id, project_name, start_date, end_date, tasks_done, leaves_taken, late_comer, in_time):
        self.name = name
        self.department = department
        self.emp_id = emp_id
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks_done = tasks_done
        self.leaves_taken = leaves_taken
        self.late_comer = late_comer
        self.in_time = in_time

    def calculate_performance(self):
        task_status = "Exuberant" if self.tasks_done == 10 else "Average" if self.tasks_done >= 5 else "Poor"
        leave_status = "Excellent" if self.leaves_taken == 0 else "Fair" if self.leaves_taken <= 2 else "Unfair"

        return task_status, leave_status

    def calculate_attendance_percentage(self):
        total_attendance = self.late_comer + self.in_time
        if total_attendance == 0:
            return 0.0
        else:
            return (self.in_time / total_attendance) * 100

def main():
    st.title("Employee Performance Calculator")

    # Input fields
    name = st.text_input("Name:")
    department = st.text_input("Department:")
    emp_id = st.text_input("Employee ID:")
    project_name = st.text_input("Project Name:")
    start_date = st.date_input("Project Starting Date:")
    end_date = st.date_input("Project Ending Date:")
    tasks_done = st.number_input("Number of Tasks Done:", min_value=0, max_value=10)
    leaves_taken = st.number_input("Number of Leaves Taken:", min_value=0)
    late_comer = st.number_input("Number of Late Comings:", min_value=0)
    in_time = st.number_input("Number of In-time Attendances:", min_value=0)

    # Create EmployeePerformanceCalculator object
    employee = EmployeePerformanceCalculator(name, department, emp_id, project_name, start_date, end_date, tasks_done, leaves_taken, late_comer, in_time)

    # Calculate performance
    task_status, leave_status = employee.calculate_performance()
    attendance_percentage = employee.calculate_attendance_percentage()

    # Display performance status
    st.write(f"Task Status: {task_status}")
    st.write(f"Leave Status: {leave_status}")
    st.write(f"Attendance Percentage: {attendance_percentage:.2f}%")

    # Bar graph
    labels = ["Tasks Done", "Leaves Taken", "Attendance Percentage"]
    values = [tasks_done, leaves_taken, attendance_percentage]
    colors = ['gold', 'lightskyblue', 'lightcoral']

    fig, ax = plt.subplots()
    bars = ax.bar(labels, values, color=colors)

    # Add labels to each bar
    for bar, value in zip(bars, values):
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, round(value, 2), ha='center', va='bottom')

    ax.set_ylabel("Count/Percentage")
    ax.set_title("Employee Performance Metrics")
    st.pyplot(fig)

if __name__ == "__main__":
    main()
