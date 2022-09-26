def updateStudentMarks(mydb, cursor, stdID):
    while True:
        test_name = input(
            "Enter the name of the test of which marks to be changed: ")
        print("Which subject's marks you wanna change?\n1.English\n2.Hindi\n3.Science\n4.SST\n5.Mathematics\nEnter Your choice", end='')
        user_choice = int(input())
        field = ''
        if user_choice == 1:
            field = 'English'
        elif user_choice == 2:
            field = 'Hindi'
        elif user_choice == 3:
            field = 'Science'
        elif user_choice == 4:
            field = 'SST'
        elif user_choice == 5:
            field = 'Maths'
        else:
            print("Enter correct Choice")
            continue
        new_value = float(input(f"Enter New Marks of {field}: "))
        try:
            cursor.execute(
                f"update {stdID} set {field}='{new_value}' where TestName='{test_name}';")
            mydb.commit()
            print("Updated Successfully...")
        except:
            print("Error encountered while update marks....Try again later")
            break
        if input(f"Wanna Update more marks details of {stdID} student? Y/N").lower() == 'n':
            break


def updateStudentDetails(mydb, cursor, searchBy, table_name):
    while True:
        print("What do you wanna Update?\n1.StudentName.\n2.RollNo.\n3.Phone Number.\n4.Address\nEnter Your choice: ", end='')
        choice = int(input())
        field = ''
        new_value = ''
        if choice == 1:
            new_value = input("Enter Student new Name: ")
            field = 'StudentName'
        elif choice == 2:
            new_value = input("Enter Student new Roll No: ")
            field = 'RollNo'
        elif choice == 3:
            new_value = input("Enter Student new Phone Number: ")
            field = 'Phone_Number'
        elif choice == 4:
            new_value = input("Enter Student new Address: ")
            field = 'Address'
        else:
            print("Make proper choice...")
            continue
        try:
            cursor.execute(
                f"update {table_name} set {field}='{new_value}' where {searchBy[1]}='{searchBy[0]}';")
            mydb.commit()
            print("Updated Successfully...")
        except:
            print("Error occured while updating details..Try again later....")
            break
        if input(f"Wanna Update more details of {searchBy[0]} student? Y/N").lower() == 'n':
            break
