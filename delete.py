def delete(mydb, cursor, stdID, tablename):
    try:
        cursor.execute(f"delete from {tablename} where StdId='{stdID}';")
        mydb.commit()
        cursor.execute(f"drop table {stdID};")
        mydb.commit()
        print("Deleted Successfully....")
    except:
        print("Error occured in deleting record..try again later....")
