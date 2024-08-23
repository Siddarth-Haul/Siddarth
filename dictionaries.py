

# A dictionary is a collection of key-value pairs.
student = {
    "name": "Rahul",
    "age": 25,
    "courses": ["Math", "Computer Science"],
    "graduated": True
}

print(f"student = {student}")

# print the different parts of the dictionary
print(f"name of student = {student['name']}")
print(f"age of student = {student['age']}")
print(f"what courses did the student have = {student['courses']}")
print(f"did student graduate = {student['graduated']}")

# add GPA key to dictionary student
student['gpa'] = 9.1
print(f"student = (student)")

# Looping over dictionaries : Method 1
print("Method 1")
for key in student:
    print(f"{key},value = {student[key]}")

print("-"*100)
# looping over dictionaries : Method 2
print("Method 2")
for key in student.keys():
    print(f"{key},value = {student[key]}")

print("-"*100)
# Looping over dictionaries : Method 3
print("Method 3")
for key, value in student.items():
    print(f"key = {key},value = {value}")

# Nested Dictionaries
# Dictionaries can contain other dictionaries, allowing for complex data structures.
students_dictionary = {
    "student1": {"name": "Rahul", "age": 25, "GPA": 8},
    "student2": {"name": "Atheendra", "age": 24, "GPA": 9},
}

print("student 1 detail:")
print(f"name = {students_dictionary['student1']['name']}")
print(f"age = {students_dictionary['student1']['age']}")
print(f"GPA = {students_dictionary['student1']['GPA']}")

print("student 2 detail:")
print(f"name = {students_dictionary['student2']['name']}")
print(f"age = {students_dictionary['student2']['age']}")
print(f"GPA = {students_dictionary['student2']['GPA']}")

print("-"*100)
print("Method 2")
for student in students_dictionary:
    print(f"name = {students_dictionary['student2']['name']}")
    print(f"age = {students_dictionary['student2']['age']}")
    print(f"GPA = {students_dictionary['student2']['GPA']}")

# List of Dictionaries
students_list = [
{"name": "Rahul", "age": 25, "GPA": 8},
{"name": "Atheendra", "age": 24, "GPA": 9}
]

# Earlier we looped over dictionary of dictionaries
# Loop over list of dictionaries
print("-"*100)
print("Method 1")
for student in students_list:
    print(f"name = {student['name']}")
    print(f"age = {student['age']}")
    print(f"GPA = {student['GPA']}")

print("-"*100)
print("Method 2")
print("-"*100)
for i in range(len(students_list)):
    print(f"name = {students_list[i]['name']}")
    print(f"age = {students_list[i]['age']}")
    print(f"GPA = {students_list[i]['GPA']}")

print("-"*100)
print("Method 3")
print("-"*100)
for index, student in enumerate(students_list):
    print(f"name of the student number {index + 1}= {students_list[i]['name']}")
    print(f"age of the student number {index + 1}= {students_list[i]['age']}")
    print(f"GPA of the student number {index + 1}= {students_list[i]['GPA']}")