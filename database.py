
def database():
    import mysql.connector as mysql
    import os
    try:
        mydb = mysql.connect(host="localhost", user=os.environ.get(
            "DB_USER"), passwd=os.environ.get("DB_PASS"))
        if mydb.is_connected():
            cursor = mydb.cursor()
            cursor.execute("use SMS;")
            cursor.execute(
                "create table if not exists signup(UserName varchar(30),pass varchar(30),ClassTeacherOf varchar(4));")
            return (mydb, cursor)
        else:
            raise Exception
    except:
        print("Error Occured.. Try after Sometime...")
        quit()
