import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64

# Function to load or create the data frame
@st.cache(allow_output_mutation=True)
def load_data():
    return pd.DataFrame(columns=['Employee Name', 'Assigned Tasks', 'Completed Tasks', 'Attendance Percentage', 'Leaves Taken', 'Performance Percentage'])

class Employee:
    def __init__(self, name, assigned_tasks, total_attendance, total_leaves):
        self.name = name
        self.assigned_tasks = assigned_tasks
        self.completed_tasks = 0
        self.total_attendance = total_attendance
        self.total_leaves = total_leaves

    def complete_task(self, tasks_completed):
        self.completed_tasks += tasks_completed

    def calculate_performance(self):
        task_performance = (self.completed_tasks / self.assigned_tasks) * 100
        attendance_percentage = (self.total_attendance / 30) * 100
        leaves_penalty = max(0, self.total_leaves - 3)
        leave_percentage = max(0, 100 - (leaves_penalty * 5))
        overall_performance = (task_performance + attendance_percentage + leave_percentage) / 3
        return overall_performance

def forecast_performance(employee):
    tasks_forecast = np.linspace(employee.completed_tasks, employee.completed_tasks * 1.2, num=5)
    forecast_data = []
    for tasks in tasks_forecast:
        forecast_performance = (tasks / employee.assigned_tasks) * 100
        attendance_percentage = (employee.total_attendance / 30) * 100
        leaves_penalty = max(0, employee.total_leaves - 3)
        leave_percentage = max(0, 100 - (leaves_penalty * 5))
        overall_forecast = (forecast_performance + attendance_percentage + leave_percentage) / 3
        forecast_data.append(overall_forecast)
    return tasks_forecast, forecast_data

def main():
    st.title("Employee Performance Calculator and Forecasting")

    # File upload for loading data
    uploaded_file = st.file_uploader("Upload Excel File (optional)", type=["xlsx", "xls"])

    # Load the data frame
    if uploaded_file is not None:
        employees_df = pd.read_excel(uploaded_file)
    else:
        employees_df = load_data()

    num_employees = st.number_input("Enter Number of Employees:", min_value=1, step=1)

    for i in range(num_employees):
        st.header(f"Employee {i + 1}")
        name = st.text_input(f"Enter Employee {i + 1} Name:")
        assigned_tasks = st.number_input(f"Enter Number of Assigned Tasks for Employee {i + 1}:", min_value=1, step=1)
        total_attendance = st.number_input(f"Enter Total Attendance for Employee {i + 1} (in days):", min_value=0, max_value=30, step=1)
        total_leaves = st.number_input(f"Enter Total Leaves for Employee {i + 1} (in days):", min_value=0, max_value=30, step=1)

        employee = Employee(name, assigned_tasks, total_attendance, total_leaves)
        employees_df = employees_df.append({
            'Employee Name': employee.name,
            'Assigned Tasks': employee.assigned_tasks,
            'Completed Tasks': employee.completed_tasks,
            'Attendance Percentage': (employee.total_attendance / 30) * 100,
            'Leaves Taken': employee.total_leaves,
            'Performance Percentage': employee.calculate_performance()
        }, ignore_index=True)

        tasks_completed = st.number_input(f"Enter Number of Completed Tasks for Employee {i + 1}:", min_value=0, step=1)
        employee.complete_task(tasks_completed)

        st.subheader(f"Forecasting for Employee {i + 1}")
        forecast_tasks, forecast_data = forecast_performance(employee)
        fig, ax = plt.subplots()
        ax.plot(forecast_tasks, forecast_data, label='Forecasted Performance')
        ax.set_xlabel('Completed Tasks')
        ax.set_ylabel('Performance Percentage')
        ax.legend()
        st.pyplot(fig)

    # Save the data frame to an Excel file
    employees_df.to_excel('employee_data.xlsx', index=False)

    st.subheader("Consolidated Employee Performance Table:")
    st.table(employees_df)

    employee_names = employees_df['Employee Name'].tolist()
    performance_percentages = employees_df['Performance Percentage'].tolist()
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(employee_names, performance_percentages)
    ax_bar.set_xlabel('Employee Name')
    ax_bar.set_ylabel('Overall Performance Percentage')
    st.pyplot(fig_bar)

    # Button to download the updated data
    st.markdown("""
    ### Download Updated Data
    Click the button below to download the updated employee data.
    """)
    st.button("Download Data", on_click=lambda: st.markdown(get_table_download_link(employees_df), unsafe_allow_html=True))

def get_table_download_link(df):
    # Function to generate a link to download a DataFrame as an Excel file
    excel_buffer = df.to_excel(index=False, encoding='utf-8')
    b64 = base64.b64encode(excel_buffer.encode()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="employee_data.xlsx">Download Excel File</a>'
    return href

if __name__ == "__main__":
    main()
