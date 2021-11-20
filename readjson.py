import json

students = []

with open('data.json', 'r') as file:
    data = json.load(file)

    for team in data.values():
        for student in team:
            students.append(student)

def get_name(student):    
    return student['name']

for student in sorted(students, key=get_name):    
    print(f'{student["name"]} - {student["choices"]}')