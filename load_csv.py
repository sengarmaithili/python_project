import csv

def load_students_csv():
    elist = []
    file = open('students.csv','r')
    reader = csv.reader(file)
    header = ('FormNumber', 'Name', 'A_rank','B_rank', 'C_rank','Degree','Percentage','Preference', 'Course_name', 'CenterID', 'Payment', 'Reported_center', 'PRN')

    def convert_student_field(field, value):
        if field == 'FormNumber' or field == 'A_rank' or field == 'B_rank' or field == 'C_rank' or field == 'Preference' or field == 'Reported_center':
            return int(value)
        elif field == 'Percentage' or field == 'Payment':
            return float(value)
        else:
            return value

    for r in reader:
        row = {}
        for key,value in zip(header,r):
            row[key] = convert_student_field(key,value)
        row['Preferred'] = []
        elist.append(row)

    return elist


def load_preferences_csv():
    elist = []
    file = open('preferences.csv','r')
    reader = csv.reader(file)
    header = ('FormNumber', 'Preference', 'Course_name', 'CenterID')

    def convert_preferences_field(field, value):
        if field == 'FormNumber' or field == 'Preference':
            return int(value)
        else:
            return value

    for r in reader:
        row = {}
        for key,value in zip(header,r):
            row[key] = convert_preferences_field(key,value)
        student = next(s for s in students if s['FormNumber'] == row['FormNumber'])
        student['Preferred'].append(row)

        elist.append(row)
    return elist

def load_eligibilities_csv():
    elist = []
    file = open('eligibilities.csv','r')
    reader = csv.reader(file)
    header = ('Course_name', 'Degree','min_Percentage' )

    def convert_eligibilities_field(field, value):
        if field == 'min_Percentage':
            return float(value)
        else:
            return value

    for r in reader:
        row = {}
        for key,value in zip(header,r):
            row[key] = convert_eligibilities_field(key,value)

        course = next(c for c in courses if c['Course_name'] == row['Course_name'])
        course['Eligibility'].append(row)

        elist.append(row)

    return elist



def load_courses_csv():
    elist = []
    file = open('courses.csv','r')
    reader = csv.reader(file)
    header = ('CourseID', 'Course_name', 'Fees', 'Section')

    def convert_courses_field(field, value):
        if field == 'CourseID' or field == 'Fees':
            return int(value)
        else:
            return value

    for r in reader:
        row = {}
        for key,value in zip(header,r):
            row[key] = convert_courses_field(key,value)
        row['Eligibility'] = []
        elist.append(row)

    return elist


def load_centers_csv():
    elist = []
    file = open('centers.csv','r')
    reader = csv.reader(file)
    header = ('CenterID','Center_name','Address','Coordinator','Password')

    for r in reader:
        row = {}
        for key,value in zip(header,r):
            row[key] = value
        row['CourseCapacity'] = {}
        elist.append(row)

    return elist


def load_capacities_csv():
    elist = []
    file = open('capacities.csv','r')
    reader = csv.reader(file)
    header = ('CenterID', 'Course_name', 'Capacity', 'Filled_Capacity')

    def convert_capacities_field(field, value):
        if field == 'Capacity' or field == 'Filled_Capacity':
            return int(value)
        else:
            return value

    for r in reader:
        row = {}
        for key,value in zip(header,r):
            row[key] = convert_capacities_field(key,value)
        center = next(c for c in centers if c['CenterID'] == row['CenterID'])
        center_capacity = center['CourseCapacity']
        center_capacity[row['Course_name']] = len(elist)
        elist.append(row)

    return elist

students = load_students_csv()
preferences = load_preferences_csv()
courses = load_courses_csv()
eligibilities = load_eligibilities_csv()
centers = load_centers_csv()
capacities = load_capacities_csv()

