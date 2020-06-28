import csv
import load_csv


def center_coordinator_sign_in():
    print(f'Enter the Center-ID and password ')
    cname = input()
    password = input()
    centers = load_csv.load_centers_csv()
    for center in centers:
        if center.get('CenterID') == cname and center.get('Password') == password:
            print('You have logged in successfully')
            return center
            break
    else:
        print('Incorrect name or password')
        return None

def center_list_courses():
    coordinator = center_coordinator_sign_in()
    load_csv.capacities = load_csv.load_capacities_csv()
    capacities = load_csv.capacities
    for capacity in capacities:
        if capacity.get('CenterID') == coordinator.get('CenterID'):
            print(capacity)

def center_list_students():
    coordinator = center_coordinator_sign_in()
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('CenterID') == coordinator.get('CenterID'):
            print(student)

def update_reported_status():
    coordinator = center_coordinator_sign_in()
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    print('Enter students form number and name')
    fnum = int(input())
    name = input()
    for student in students:
        if student.get('CenterID') == coordinator.get('CenterID'):
            if student.get('FormNumber') == fnum and student.get('Name') == name:
                student['FormNumber'] = student.get('FormNumber')
                student['Name'] = student.get('Name')
                student['A_rank'] = student.get('A_rank')
                student['B_rank'] = student.get('B_rank')
                student['C_rank'] = student.get('C_rank')
                student['Degree'] = student.get('Degree')
                student['Percentage'] = student.get('Percentage')
                student['Preference'] = student.get('Preference')
                student['Course_name'] = student.get('Course_name')
                student['CenterID'] = student.get('CenterID')
                student['Payment'] = student.get('Payment')
                student['Reported_center'] = 1
                student['PRN'] = student.get('PRN')

    with open("students.csv", 'w') as file:
        round1 = csv.writer(file)
        for s in students:
            round1.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'], s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'], s['Reported_center'], s['PRN']])


def list_admitted_students():
    coordinator = center_coordinator_sign_in()
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('CenterID') == coordinator.get('CenterID') and student.get('PRN') != 'NA':
            print(student)
