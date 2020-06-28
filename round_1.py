import csv
import load_csv

def rankA(students, capacities,i):
    students.sort(key=lambda x:x.get('A_rank'))
    for student in students:
        prefer = student.get('Preferred')
        for p in prefer:
            if p.get('Preference') == i and p.get('Course_name') == 'PG-DGI' and student.get('Preference')==0 and student.get('Payment') != -1:
                for capacity in capacities:
                    if capacity.get('CenterID') == p.get('CenterID') and capacity.get('Course_name') == p.get('Course_name') and (capacity.get('Capacity') > capacity.get('Filled_Capacity')):
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
                        student['PRN'] = student.get('PRN')
                        capacity['Filled_Capacity'] += 1

    with open("capacities.csv", 'w') as file:
        round1 = csv.writer(file)
        for c in capacities:
            round1.writerow([c['CenterID'], c['Course_name'], c['Capacity'], c['Filled_Capacity']])

    with open("students.csv", 'w') as file:
        round1 = csv.writer(file)
        for s in students:
            round1.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'],s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'],s['Reported_center'], s['PRN']])


def rankB(students, capacities, i):
    students.sort(key=lambda x:x.get('B_rank'))
    for student in students:
        prefer = student.get('Preferred')
        for p in prefer:
            if p.get('Preference') == i and student.get('Preference')==0  and student.get('Payment') == 0.0 and (p.get('Course_name') == 'PG-DAC' or p.get('Course_name') == 'PG-DMC' or p.get('Course_name') == 'PG-DBDA') :
                for capacity in capacities:
                    if capacity.get('CenterID') == p.get('CenterID') and capacity.get('Course_name') == p.get('Course_name') and (capacity.get('Capacity') > capacity.get('Filled_Capacity')):
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
                        student['PRN'] = student.get('PRN')
                        capacity['Filled_Capacity'] += 1

    with open("capacities.csv", 'w') as file:
        round1 = csv.writer(file)
        for c in capacities:
            round1.writerow([c['CenterID'], c['Course_name'], c['Capacity'], c['Filled_Capacity']])

    with open("students.csv", 'w') as file:
        round1 = csv.writer(file)
        for s in students:
            round1.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'], s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'], s['Reported_center'], s['PRN']])


def rankC(students, capacities, i):
    students.sort(key=lambda x:x.get('C_rank'))
    for student in students:
        prefer = student.get('Preferred')
        for p in prefer:
            if p.get('Preference') == i and student.get('Preference')==0 and student.get('Payment') == 0.0 and (p.get('Course_name') == 'PG-DESD'):
                for capacity in capacities:
                    if capacity.get('CenterID') == p.get('CenterID') and capacity.get('Course_name') == p.get('Course_name') and (capacity.get('Capacity') > capacity.get('Filled_Capacity')):
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
                        student['PRN'] = student.get('PRN')
                        capacity['Filled_Capacity'] += 1

    with open("capacities.csv", 'w') as file:
        round1 = csv.writer(file)
        for c in capacities:
            round1.writerow([c['CenterID'], c['Course_name'], c['Capacity'], c['Filled_Capacity']])

    with open("students.csv", 'w') as file:
        round1 = csv.writer(file)
        for s in students:
            round1.writerow([s['FormNumber'], s['Name'], s['A_rank'],s['B_rank'], s['C_rank'],s['Degree'],s['Percentage'],s['Preference'], s['Course_name'], s['CenterID'], s['Payment'], s['Reported_center'], s['PRN']])


def round_1():
    load_csv.students = load_csv.load_students_csv()
    load_csv.preferences = load_csv.load_preferences_csv()
    students = load_csv.students

    load_csv.capacities = load_csv.load_capacities_csv()
    capacities = load_csv.capacities

    for i in range(11):
        rankA(students,capacities,i)
        rankB(students,capacities,i)
        rankC(students, capacities,i)

