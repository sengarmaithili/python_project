import csv
import load_csv
import round_1
import round_2

def admin_sign_in():
    print(f'Enter the username and password ')
    uname = input()
    password = input()
    if uname == 'admin' and password == 'admin':
        return True
    else:
        return False

def courses_eligibilities_list():
    courses = load_csv.load_courses_csv()
    for cor in courses:
        print(cor)
    eligibilities = load_csv.load_eligibilities_csv()
    for elig in eligibilities:
        print(elig)

def centers_capacities_list():
    centers = load_csv.load_centers_csv()
    capacities = load_csv.load_capacities_csv()
    for cen in centers:
        print(cen)
    for cap in capacities:
        print(cap)

def student_list():
    print('List of students is given below :')
    student = load_csv.load_students_csv()
    for s in student:
        print(s)

def update_rank():
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    students.sort(key=lambda x:x.get('A_rank'),reverse=True)
    A_max = students[0].get('A_rank')
    students.sort(key=lambda x:x.get('B_rank'),reverse=True)
    B_max = students[0].get('B_rank')
    students.sort(key=lambda x:x.get('C_rank'),reverse=True)
    C_max = students[0].get('C_rank')
    for student in students:
        if student.get('A_rank') == 0 or student.get('B_rank') == 0 or student.get('C_rank') == 0:
            student['FormNumber'] = student.get('FormNumber')
            student['Name'] = student.get('Name')
            if student.get('A_rank') == 0:
                A_max += 1
                student['A_rank'] = A_max
            else:
                student['A_rank'] = student.get('A_rank')
            if student.get('B_rank') == 0:
                B_max += 1
                student['B_rank'] = B_max
            else:
                student['B_rank'] = student.get('B_rank')
            if student.get('C_rank') == 0:
                C_max += 1
                student['C_rank'] = C_max
            else:
                student['C_rank'] = student.get('C_rank')

            student['Degree'] = student.get('Degree')
            student['Percentage'] = student.get('Percentage')
            student['Preference'] = student.get('Preference')
            student['Course_name'] = student.get('Course_name')
            student['CenterID'] = student.get('CenterID')
            student['Payment'] = student.get('Payment')
            student['Reported_center'] = student.get('Reported_center')
            student['PRN'] = student.get('PRN')

    with open("students.csv", 'w') as file:
        rank = csv.writer(file)
        for s in students:
            rank.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'], s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'], s['Reported_center'], s['PRN']])



def round1():
    round_1.round_1()

def round2():
    round_2.round_2()

def list_allocated_students():
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('Preference') != 0 :
            print(student)

def list_paid_student():
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('Preference') != 0 and student.get('Payment') == 11800:
            print(student)


def center_reported_student():
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('Preference') != 0 and student.get('Reported_center') != 0:
            print(student)


def generate_PRN():
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('Preference') != 0 and student.get('Reported_center') != 0 and (student.get('Payment') == 94000 or student.get('Payment') == 80000 or student.get('Payment') == 115000):
            student['FormNumber'] = student.get('FormNumber')
            student['Name'] = student.get('Name')
            student['A_rank'] = student.get('A_rank')
            student['B_rank'] = student.get('B_rank')
            student['C_rank'] = student.get('C_rank')
            student['Degree'] = student.get('Degree')
            student['Percentage'] = student.get('Percentage')
            student['Preference'] = p.get('Preference')
            student['Course_name'] = p.get('Course_name')
            student['CenterID'] = p.get('CenterID')
            student['Payment'] = student.get('Payment')
            student['Reported_center'] = student.get('Reported_center')

            cen = student.get('CenterID')
            cor = student.get('Course_name')
            srno = student.get('FormNumber')
            prn = [cen,'_' , cor, '_' , str(srno)]
            student['PRN'] = ''.join(prn)
            print([student['FormNumber'], student['Name'], student['PRN']])

    with open("students.csv", 'w') as file:
        write = csv.writer(file)
        for s in students:
            write.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'],s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'],s['Reported_center'], s['PRN']])


def addmitted_student_PRN(center):
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    for student in students:
        if student.get('CenterID') == center and student.get('PRN') != 'NA':
            print(student)
