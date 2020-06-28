import csv
import student
import admin
import center_coordinator

def main_menu():
    print("Welcome user...")
    print("0. Exit")
    print("1. Student")
    print("2. Admin")
    print("3. Center coordinator")
    print("Please select your option: ")
    choice = int(input())
    return choice

def student_menu():
    print("0. Go back to main menu")
    print("1. Register new student")
    print("2. Sign in")
    print("3. List courses")
    print("4.List centers")
    print("5.Give preferences")
    print("6.See allocated center/course")
    print("7.Update payment details")
    print("Please select your option: ")
    choice = int(input())
    return choice

def admin_menu():
    print("0. Go back to main menu")
    print("1. Sign in")
    print("2. List courses and eligibilities")
    print("3.List centers and capacities")
    print("4.List students")
    print("5.Update student ranks")
    print("6.Allocate centers (Round 1)")
    print("7.Allocate centers (Round 2)")
    print("8.List allocated students")
    print("9.List paid students")
    print("10.List reported (at center) students")
    print("11.Generate PRN")
    print("12.List admitted students (with PRN) for given center")
    print("Please select your option: ")
    choice = int(input())
    return choice


def center_coordinator_menu():
    print("0. Go back to main menu")
    print("1. Sign in")
    print("2. List courses")
    print("3.List students")
    print("4.Update reported status")
    print("5.List admitted students (with PRN)")
    print("Please select your option: ")
    choice = int(input())
    return choice


def menu():
    while True:
        choice = main_menu()
        if choice == 1:
            while True:
                c = student_menu()
                if c == 1:
                    student.register_new()

                elif c == 2:
                    s = student.student_sign_in()
                    print(s)

                elif c == 3:
                    course = student.courses_list_if_eligible()
                    print('Given below is the list of courses according to your eligibility')
                    for cor in course:
                        print(cor)

                elif c == 4:
                    center = student.centers_list()
                    print('Given below is the list of centers according to eligile course')
                    for cen in center:
                        print(cen)

                elif c == 5:
                    prefer = student.prefernces_give()
                    with open('preferences.csv','a') as aobj:
                        add = csv.writer(aobj)
                        add.writerow(prefer)
                    print('Preference added successfully')

                elif c == 6:
                    a = student.allocated_center_course()
                    print(f'Your allocated center is:\n Course name = {a[0]} \t Center ID = {a[1]} ')

                elif c == 7:
                    student.update_payment()
                    print('Your payment status is updated successfully')

                elif c == 0:
                    break

                else:
                    print("You have entered a wrong option")
                print("Press Enter to Continue...")
                input()

        elif choice == 2:
            while True:
                c = admin_menu()

                if c == 1:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 2:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('List of courses and eligibilities')
                        admin.courses_eligibilities_list()
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 3:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('List of centers and capacities')
                        admin.centers_capacities_list()
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 4:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        print('List of all the students')
                        admin.student_list()

                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 5:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        admin.update_rank()
                        print('All the ranks are updated Successfully')
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 6:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        admin.round1()
                        print('Round 1 allocation done successfully')
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 7:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        admin.round2()
                        print('Round 2 allocation done successfully')
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 8:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        print('List of all the allocated students is given below:')
                        admin.list_allocated_students()

                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 9:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        print('List of students fees paid is given below:')
                        admin.list_paid_student()
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 10:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        print('List of students reported at corresponding centers is given below:')
                        admin.center_reported_student()
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 11:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        admin.generate_PRN()
                        print('PRN of students generated successfully')
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 12:
                    a = admin.admin_sign_in()
                    if a == True:
                        print('You have logged in successfully')
                        print('Enter the center ID')
                        center = input()
                        print(f'List of admitted students (with PRN) for {center} center is:')
                        admin.addmitted_student_PRN(center)
                    else:
                        print('Incorrect username or password. Please try again')

                elif c == 0:
                    break
                else:
                    print("You have entered a wrong option")
                print("Press Enter to Continue...")
                input()

        elif choice == 3:
            while True:
                c = center_coordinator_menu()
                if c == 1:
                    coordinator = center_coordinator.center_coordinator_sign_in()
                    print(coordinator)
                elif c == 2:
                    print('List of courses at that center is:')
                    center_coordinator.center_list_courses()

                elif c == 3:
                    print('List of students alloacted at this center is:')
                    center_coordinator.center_list_students()
                elif c == 4:
                    center_coordinator.update_reported_status()
                    print('Reported student status updated successfully')
                elif c == 5:
                    print('List of admitted students with their PRN are given below:')
                    center_coordinator.list_admitted_students()
                elif c == 0:
                    break
                else:
                    print("You have entered a wrong option")
                print("Press Enter to Continue...")
                input()
        elif choice == 0:
            print("exiting....")
            break

        else:
            print("You have entered a wrong option")

        print("Press Enter to Continue...")
        input()


if __name__ == '__main__':
    menu()
