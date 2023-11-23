import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class EmployeePerformanceCalculator:
    def __init__(self, name, department, emp_id, project_name, start_date, end_date, tasks_assigned, tasks_completed, tasks_in_progress, leaves_taken, login_time):
        self.name = name
        self.department = department
        self.emp_id = emp_id
        self.project_name = project_name
        self.start_date = start_date
        self.end_date = end_date
        self.tasks_assigned = tasks_assigned
        self.tasks_completed = tasks_completed
        self.tasks_in_progress = tasks_in_progress
        self.leaves_taken = leaves_taken
        self.login_time = login_time

    def calculate_performance(self):
        task_status = "Exuberant" if self.tasks_completed == self.tasks_assigned else "Average" if self.tasks_completed >= self.tasks_assigned / 2 else "Poor"
        leave_status = "Excellent" if self.leaves_taken == 0 else "Fair" if self.leaves_taken <= 2 else "Unfair"
        attendance_status = "In Time" if self.login_time <= 9.30 else "Late Comer"

        return task_status, leave_status, attendance_status

    def calculate_task_progress_percentage(self):
        if self.tasks_assigned == 0:
            return 0.0
        else:
            return (self.tasks_completed / self.tasks_assigned) * 100

def main():
    st.title("Employee Performance Calculator")

    # Data storage
    student_data = []

    # Function to add a new student
    def add_student():
        name = st.text_input("Name:")
        department = st.text_input("Department:")
        emp_id = st.text_input("Employee ID:")
        project_name = st.text_input("Project Name:")
        start_date = st.date_input("Project Starting Date:")
        end_date = st.date_input("Project Ending Date:")
        tasks_assigned = st.number_input("Number of Tasks Assigned:", min_value=0)
        tasks_completed = st.number_input("Number of Tasks Completed:", min_value=0, max_value=tasks_assigned)
        tasks_in_progress = st.number_input("Number of Tasks in Progress:", min_value=0, max_value=tasks_assigned - tasks_completed)
        leaves_taken = st.number_input("Number of Leaves Taken:", min_value=0)
        login_time = st.number_input("Login Time (24-hour format):", min_value=0, max_value=24, step=0.01)

        student = EmployeePerformanceCalculator(name, department, emp_id, project_name, start_date, end_date, tasks_assigned, tasks_completed, tasks_in_progress, leaves_taken, login_time)
        student_data.append(student)

    # Button to add a new student
    if st.button("Add Student"):
        add_student()

    # Display details as a table
    if student_data:
        st.subheader("Student Details")
        df = pd.DataFrame([vars(student) for student in student_data])
        st.table(df)

        # Calculate overall performance metrics for all students
        overall_tasks_assigned = sum(student.tasks_assigned for student in student_data)
        overall_tasks_completed = sum(student.tasks_completed for student in student_data)
        overall_tasks_in_progress = sum(student.tasks_in_progress for student in student_data)
        overall_leaves_taken = sum(student.leaves_taken for student in student_data)
        overall_task_progress_percentage = (overall_tasks_completed / overall_tasks_assigned) * 100 if overall_tasks_assigned > 0 else 0.0

        # Display overall performance status
        st.subheader("Overall Performance Metrics")
        st.text(f"Overall Task Progress Percentage: {overall_task_progress_percentage:.2f}%")
        st.text(f"Overall Leaves Taken: {overall_leaves_taken}")

        # Bar graph
        labels = ["Tasks Assigned", "Tasks Completed", "Tasks in Progress", "Leaves Taken", "Task Progress Percentage"]
        values = [overall_tasks_assigned, overall_tasks_completed, overall_tasks_in_progress, overall_leaves_taken, overall_task_progress_percentage]
        colors = ['gold', 'lightskyblue', 'lightgreen', 'lightcoral', 'lightpink']

        fig, ax = plt.subplots()
        bars = ax.bar(labels, values, color=colors)

        # Add labels to each bar
        for bar, value in zip(bars, values):
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval, round(value, 2), ha='center', va='bottom')

        ax.set_ylabel("Count/Percentage")
        ax.set_title("Overall Performance Metrics")

        # Display the plot using st.pyplot()
        st.pyplot(fig)

if __name__ == "__main__":
    main()
