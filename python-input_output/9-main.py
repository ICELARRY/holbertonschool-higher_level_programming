#!/usr/bin/python3
"""
9-main.py
Test the Student class and its to_json method
"""

Student = __import__('9-student').Student

# Create a list of students
students = [Student("John", "Doe", 23), Student("Bob", "Dylan", 27)]

# Loop through each student and print their JSON dictionary
for student in students:
    j_student = student.to_json()
    print(type(j_student))
    print(j_student['first_name'])
    print(type(j_student['first_name']))
    print(j_student['age'])
    print(type(j_student['age']))
