def AddStudDetails(mycon, cursor, tablename):
    stdID = input("Enter Student Unique ID: ")
    studName = input("Enter Student Name: ")
    rollNo = int(input("Enter Roll No: "))
    phno = int(input("Enter Student Phone Number: "))
    address = input("Enter Student Home Address...")
    motherName = input("Enter Mother's Name: ")
    fatherName = input("Enter Father's Name: ")
    dob = input("Enter DOB in YYYY-MM-DD: ")
    try:
        cursor.execute(
            f'insert into {tablename} (StdId,StudentName,RollNo,Phone_Number,Address,MotherName,FatherName,DOB) values("{stdID}","{studName}",{rollNo},{phno},"{address}","{motherName}","{fatherName}","{dob}");')
        mycon.commit()
        print("Added Successfully")
    except:
        print("Error occured while inserting student record....try again later")


def AddStudSubMarksDeatils(mydb, cursor, stdID):
    try:
        # cursor.execute("create database if not exists SMS_STUDENTS;")
        # mydb.commit()
        # cursor.execute("use SMS_STUDENTS;")
        cursor.execute(
            f"create table if not exists {stdID} (English double(5,2),Hindi double(5,2),Science double(5,2),SST double(5,2),Maths double(5,2),TestName varchar(10));")
    except:
        print("Error Occured in add marks details of student..Try again later...")
        return
    eng = float(input("Enter English Marks: "))
    hindi = float(input("Enter Hindi Marks: "))
    science = float(input("Enter Science Marks: "))
    sst = float(input("Enter SST Marks: "))
    maths = float(input("Enter Maths Marks: "))
    testname = input("Enter Name of the Test for which marks are recorded: ")
    try:
        cursor.execute(
            f"insert into {stdID} values({eng},{hindi},{science},{sst},{maths},'{testname}')")
        mydb.commit()
        print("Added Successfully")
    except:
        print("Error occured while inserting marks.")
        return
