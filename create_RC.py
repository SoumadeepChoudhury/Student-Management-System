def RC(cursor, stdID, table_name):
    try:
        # cursor.execute("use SMS_STUDENTS;")
        test_name = input(
            "Enter the name of the test for which you wanna display the report card: ")
        cursor.execute(f"select * from {stdID} where TestName='{test_name}';")
        eng, hindi, science, sst, maths, _ = cursor.fetchall()[0]
        # cursor.execute("use SMS;")
        cursor.execute(
            f"select StudentName,Class,MotherName,FatherName,DOB from {table_name} where StdId='{stdID}'")
        name, class_, mother_name, father_name, dob = cursor.fetchall()[0]
        longerVal = ''
        if len(name) > len(father_name):
            longerVal = name
        else:
            longerVal = father_name
        total_marks = eng+hindi+science+sst+maths
        percentage = total_marks/5
        grade = ''
        if percentage <= 40:
            grade = 'D'
        elif percentage > 40 and percentage <= 50:
            grade = 'C'
        elif percentage > 50 and percentage <= 60:
            grade = 'C+'
        elif percentage > 60 and percentage < 70:
            grade = 'B'
        elif percentage > 71 and percentage < 80:
            grade = 'B+'
        elif percentage > 80 and percentage < 90:
            grade = 'A'
        elif percentage > 90:
            grade = 'A+'
        print(f"_____________REPORT CARD______________\nName{' '*(18-len('Name'))}: {name+(' '*(len(longerVal)+5-len(name)))}Class{' '*(16-len('Class'))}: {class_}\nFather's Name{' '*(18-len('Father s Name'))}: {father_name+(' '*(len(longerVal)+5-len(father_name)))}Mother's Name{' '*(16-len('Mother s Name'))}: {mother_name}\nDate of Birth{' '*(18-len('Date of Birth'))}: {dob}\nEnglish{' '*(18-len('English'))}: {eng}\nHindi{' '*(18-len('Hindi'))}: {hindi}\nScience{' '*(18-len('Science'))}: {science}\nSocial Studies{' '*(18-len('Social Studies'))}: {sst}\nMathematics{' '*(18-len('Mathematics'))}: {maths}\nTotal Marks{' '*(18-len('Total Marks'))}: {total_marks}\nPercentage{' '*(18-len('Percentage'))}: {percentage}\nOverall Grade{' '*(18-len('Overall Grade'))}: {grade}")

    except:
        print("Error occured while Displaying the report card...")
        return
