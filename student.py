import csv
import load_csv

def register_new():
    validity = 0
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    students.sort(key=lambda x:x.get('FormNumber'),reverse=True)
    max = students[0].get('FormNumber')
    form_no = max + 1
    print('Enter your name')
    name = input()
    print('Enter the category (A or B or C)')
    category = input()
    if category == 'A':
        A = 0; B = -1; C = -1
    elif category == 'B':
        A = 0; B = 0; C = -1
    elif category == 'C':
        A = 0; B = 0; C = 0
    else:
        validity = 1
    print('Enter your quailified degree')
    degree = input()
    degree_list = []
    with open('degrees.txt', 'r') as file:
        for line in file:
            degree_list.append(line.replace('\n', ''))
    for d in degree_list:
        if d == degree:
            print('Enter percentage corresponding to the degree')
            percent = float(input())
            break
    else:
        validity = 1

    if validity == 0:
        new = [form_no, name, A, B, C, degree, percent, 0, 'NA', 'NA', 0, 0, 'NA']
        with open('students.csv', 'a') as aobj:
            add = csv.writer(aobj)
            add.writerow(new)
        print('Student registered successfully')
    else:
        print('Invalid category or degree. Try again')


def student_sign_in():
    print(f'Enter the form number and name ')
    fnumber = int(input())
    name = input()
    student = load_csv.load_students_csv()
    for s in student:
        if s.get('FormNumber') == fnumber and s.get('Name') == name:
            print('You have signed in successfully')
            return s
            break
    else:
        print('Incorrect form number or name')
        return None

def courses_list_if_eligible():
    s = student_sign_in()
    eligibility = load_csv.load_eligibilities_csv()
    clist = []
    for e in eligibility:
        if s.get('Degree') == e.get('Degree') and s.get('Percentage') >= e.get('min_Percentage'):
            if e.get('Course_name') == 'PG-DGI':
                clist.append(e.get('Course_name'))
            elif e.get('Course_name') == 'PG-DESD' and s.get('C_rank') != -1:
                clist.append(e.get('Course_name'))
            elif e.get('Course_name') == 'PG-DAC' and s.get('B_rank') != -1:
                clist.append(e.get('Course_name'))
            elif e.get('Course_name') == 'PG-DMC' and s.get('B_rank') != -1:
                clist.append(e.get('Course_name'))
            elif e.get('Course_name') == 'PG-DBDA' and s.get('B_rank') != -1:
                clist.append(e.get('Course_name'))

    return clist

def centers_list():
    course = courses_list_if_eligible()
    capacity = load_csv.load_capacities_csv()
    cen = []
    for cor in course:
        for cap in capacity:
            if cor == cap.get('Course_name'):
                cen.append(cap.get('CenterID'))
    return list(set(cen))

def prefernces_give():
    s = student_sign_in()
    load_csv.students = load_csv.load_students_csv()
    load_csv.preferences = load_csv.load_preferences_csv()
    students = load_csv.students
    for stud in students:
        if s.get('FormNumber') == stud.get('FormNumber'):
            prefers = stud.get('Preferred')
    prefers.sort(key=lambda x:x.get('Preference'))
    pref = len(prefers)+1

    if pref <= 10:

        eligibility = load_csv.load_eligibilities_csv()
        clist = []
        for e in eligibility:
            if s.get('Degree') == e.get('Degree') and s.get('Percentage') >= e.get('min_Percentage'):
                if e.get('Course_name') == 'PG-DGI':
                    clist.append(e.get('Course_name'))
                elif e.get('Course_name') == 'PG-DESD' and s.get('C_rank') != -1:
                    clist.append(e.get('Course_name'))
                elif e.get('Course_name') == 'PG-DAC' and s.get('B_rank') != -1:
                    clist.append(e.get('Course_name'))
                elif e.get('Course_name') == 'PG-DMC' and s.get('B_rank') != -1:
                    clist.append(e.get('Course_name'))
                elif e.get('Course_name') == 'PG-DBDA' and s.get('B_rank') != -1:
                    clist.append(e.get('Course_name'))

        capacity = load_csv.load_capacities_csv()
        cen = []
        for c in clist:
            for cap in capacity:
                if c == cap.get('Course_name'):
                    cen.append([cap.get('Course_name'), cap.get('CenterID')])
        similar = []
        for p in prefers:
            l = [p.get('Course_name'), p.get('CenterID')]
            for c in cen:
                if l == c:
                    similar.append(l)
        for sim in similar:
            cen.remove(sim)

        print('options available for prefernces is :')
        counter = 0
        for c in cen:
            c.insert(0,counter+1)
            counter += 1
            print(f'{c[0]}. {c[1]}  {c[2]}')
        print('please enter the correct option number ')
        i = int(input())

        d = [s.get('FormNumber'),pref,cen[i-1][1],cen[i-1][2]]
    return d


def allocated_center_course():
    s = student_sign_in()
    stud_list = load_csv.students
    for stud in stud_list:
        if s.get('FormNumber') == stud.get('FormNumber'):
            return [stud.get('Course_name'), stud.get('CenterID')]

def update_payment():
    s = student_sign_in()
    load_csv.students = load_csv.load_students_csv()
    students = load_csv.students
    print('Enter the amount to be paid')
    pay = int(input())
    for student in students:
        if student.get('FormNumber') == s.get('FormNumber') and student.get('Name') == s.get('Name'):
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
            student['Payment'] = pay
            student['Reported_center'] = student.get('Reported_center')
            student['PRN'] = student.get('PRN')

    with open("students.csv", 'w') as file:
        round1 = csv.writer(file)
        for s in students:
            round1.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'], s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'], s['Reported_center'], s['PRN']])

