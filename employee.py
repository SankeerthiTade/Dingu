import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

class Employee:
    # ... (unchanged)

def forecast_performance(employee):
    # Assuming a linear growth trend for the completed tasks
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

    # ... (unchanged)

    for i, employee in enumerate(employees):
        # ... (unchanged)

        # Input for completed tasks
        tasks_completed = st.number_input(f"Enter Number of Completed Tasks for Employee {i + 1}:", min_value=0, step=1)
        employee.complete_task(tasks_completed)

        # Display forecasting view
        st.subheader(f"Forecasting for Employee {i + 1}")
        forecast_tasks, forecast_data = forecast_performance(employee)
        fig, ax = plt.subplots()
        ax.plot(forecast_tasks, forecast_data, label='Forecasted Performance')
        ax.set_xlabel('Completed Tasks')
        ax.set_ylabel('Performance Percentage')
        ax.legend()
        st.pyplot(fig)

    # Display consolidated table
    st.subheader("Consolidated Employee Performance Table:")
    st.table(performance_data)

    # Display bar graph for overall performance
    employee_names = [employee.name for employee in employees]
    performance_percentages = [employee.calculate_performance() for employee in employees]
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(employee_names, performance_percentages)
    ax_bar.set_xlabel('Employee Name')
    ax_bar.set_ylabel('Overall Performance Percentage')
    st.pyplot(fig_bar)

if __name__ == "__main__":
    main()
