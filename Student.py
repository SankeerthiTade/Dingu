import streamlit as st
 
# Base Class: Student
class Student:
    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade
 
    def display_details(self):
        st.write(f"Student Name: {self._name}")
        st.write(f"Student Age: {self._age}")
        st.write(f"Student Grade: {self._grade}")
 
 
# Derived Class: StudentMarks (Inherits from Student)
class StudentMarks(Student):
    def __init__(self, name, age, grade, marks):
        super().__init__(name, age, grade)
        self._marks = marks
 
    def display_details(self):
        super().display_details()
        st.write(f"Student Marks: {self._marks}")
 
 
# Streamlit UI
def main():
    st.title("Student Details and Marks")
 
    # User input for student details
    name = st.text_input("Enter Student Name:")
    age = st.number_input("Enter Student Age:")
    grade = st.text_input("Enter Student Grade:")
 
    # User input for marks
    marks = st.text_input("Enter Student Marks:")
 
    # Create an instance of StudentMarks
    student = StudentMarks(name, age, grade, marks)
 
    # Display student details and marks
    student.display_details()
 
 
if __name__ == "__main__":
    main()
