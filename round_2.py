import csv
import load_csv
import round_1

def update(students, capacities):
    for student in students:
        if student.get('Preference') != 0 and student.get('Payment') != 11800:
            for capacity in capacities:
                if capacity.get('CenterID') == student.get('CenterID') and capacity.get('Course_name') == student.get('Course_name'):
                    student['FormNumber'] = student.get('FormNumber')
                    student['Name'] = student.get('Name')
                    student['A_rank'] = student.get('A_rank')
                    student['B_rank'] = student.get('B_rank')
                    student['C_rank'] = student.get('C_rank')
                    student['Degree'] = student.get('Degree')
                    student['Percentage'] = student.get('Percentage')
                    student['Preference'] = 0
                    student['Course_name'] = 'NA'
                    student['CenterID'] = 'NA'
                    student['Payment'] = -1
                    student['Reported_center'] = student.get('Reported_center')
                    student['PRN'] = student.get('PRN')
                    capacity['Filled_Capacity'] -= 1

    with open("capacities.csv", 'w') as file:
        round1 = csv.writer(file)
        for c in capacities:
            round1.writerow([c['CenterID'], c['Course_name'], c['Capacity'], c['Filled_Capacity']])

    with open("students.csv", 'w') as file:
        round2 = csv.writer(file)
        for s in students:
            round2.writerow([s['FormNumber'], s['Name'], s['A_rank'], s['B_rank'], s['C_rank'], s['Degree'],s['Percentage'], s['Preference'], s['Course_name'], s['CenterID'], s['Payment'],s['Reported_center'], s['PRN']])


def round_2():
    load_csv.students = load_csv.load_students_csv()
    load_csv.preferences = load_csv.load_preferences_csv()
    students = load_csv.students

    load_csv.capacities = load_csv.load_capacities_csv()
    capacities = load_csv.capacities

    update(students,capacities)
    round_1.round_1()

