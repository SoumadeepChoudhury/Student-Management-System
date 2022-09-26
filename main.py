from update import updateStudentDetails, updateStudentMarks
from delete import delete
from create_RC import RC
from sign_up_in import signup, signin
from add_stud import AddStudDetails, AddStudSubMarksDeatils
from database import database
mydb, cursor = database()
cond = False
teacher_of, userName = '', ''
print("......WELCOME TO SMS......")
while cond == False:
    print("1. Sign Up\n2. Sign In\nEnter Your choice.... ", end='')
    choice = int(input())
    if choice == 1:
        userName, teacher_of = signup(mydb, cursor)
        cond = True
    else:
        cond, userName, teacher_of = signin(cursor)
        userName = ''.join(userName.split())
if cond:
    while True:
        choice = int(input("You can do the following here:::\n1. Add new record of Student\n2. Update record of Student\n3. Add subject details of student a create report card.\n4. View the Report of a Student.\n5. Delete Student record\n6. Log Out\nEnter Your choice: "))
        if choice == 1:
            AddStudDetails(mydb, cursor, userName+teacher_of)
        elif choice == 2:
            print("What do you want to update?\n1. Student Record...\n2. Student Marks..\nEnter Your Choice.. ", end='')
            subchoice = int(input())
            if subchoice == 1:
                tempChoice = int(input(
                    "Update Student Details via :\n1. Student Unique ID\n2. Roll No.\nEnter Your choice: "))
                if tempChoice == 1:
                    searchBy = (input("Enter Student ID: "), "StdId")
                else:
                    searchBy = (input("Enter Roll No: "), "RollNo")
                updateStudentDetails(
                    mydb, cursor, searchBy, userName+teacher_of)
            if subchoice == 2:
                stdID = input("Enter Student Unique ID: ")
                updateStudentMarks(mydb, cursor, stdID)
        elif choice == 3:
            stdID = input("Enter Student's Unique ID: ")
            AddStudSubMarksDeatils(mydb, cursor, stdID)
        elif choice == 4:
            stdID = input("Enter Student's Unique ID: ")
            RC(cursor, stdID, userName+teacher_of)
        elif choice == 5:
            stuID = input("Enter Student Unique ID: ")
            delete(mydb, cursor, stdID, userName+teacher_of)
        else:
            print("Logged Out.")
            quit()
