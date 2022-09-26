def signin(cursor):
    userName = input("Enter User name of Administrator: ")
    password = input("Enter Strong Administrative Password: ")
    teacher_of = ''
    try:
        cursor.execute(
            f"select UserName,pass,ClassTeacherOf from signup where UserName='{userName}'")
        for i in cursor:
            if i[0] == userName and i[1] == password:
                teacher_of = i[2]
                return (True, userName, teacher_of)
            else:
                print("Incorrect User Name and Password......")
                return (False, userName, teacher_of)
        else:
            print("No User Found...")
            return (False, userName, teacher_of)
    except:
        print("No User Found....")
        return False


def signup(mydb, cursor):
    while True:
        userName = input("Enter User name of Administrator: ")
        password = input("Enter Strong Administrative Password: ")
        teacher_of = input("You are teacher of which class and section?: ")
        if userName != '' and password != '' and teacher_of != '':
            try:
                cursor.execute(
                    f"insert into signup values('{userName}','{password}','{teacher_of}');")
                mydb.commit()
                userName = ''.join(userName.split())
                cursor.execute(
                    f"create table if not exists {userName+teacher_of} (StdId char(6) primary key, StudentName varchar(30),Class varchar(4) DEFAULT '{teacher_of}',RollNo int,Phone_Number int(10),Address varchar(30),MotherName varchar(30),FatherName varchar(30),DOB date);")
            except:
                print("Error Occured while signing up....")
                quit()
            return (userName, teacher_of)
        else:
            print("Enter details correctly...")
            continue
