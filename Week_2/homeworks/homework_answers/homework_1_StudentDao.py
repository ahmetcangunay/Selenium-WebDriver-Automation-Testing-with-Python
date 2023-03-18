import homework_1_Student as stu
import sqlite3


class StudentDao():

    def create_table(self, db_name):

        global con
        global cur
        con = sqlite3.connect(db_name)
        cur = con.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS student(Name, Surname)")

    def get_all_students(self):

        res = cur.execute("SELECT * FROM student")
        print("Student List:")

        for idx, name in enumerate(res.fetchall(), start=1):
            print(f"{idx} {name[0]} {name[1]}")

    def get_student_number_by_name(self, name):
        res = cur.execute("select *, ROW_NUMBER() OVER() AS NoId from student")
        for i in res.fetchall():
            if i[0] == name:
                print(f"Student: {i[0]} {i[1]}, is on the list as {i[2]}")
            else:
                continue

    def add_student(self, name, surname):
        cur.execute("INSERT INTO student VALUES(?, ?)", (name, surname))
        con.commit()

    def delete_student(self, name, surname):
        cur.execute(
            f"DELETE FROM student WHERE Name='{name}' AND Surname='{surname}'")
        con.commit()

    def add_multiple_student(self, student_list):
        cur.executemany("INSERT INTO student VALUES(?, ?)", student_list)
        con.commit()

    def delete_multiple_student(self, student_list):

        i = 0

        while(i < len(student_list)):

            cur.execute(
                f"DELETE FROM student WHERE Name='{student_list[i][0]}' AND Surname='{student_list[i][1]}'")
            con.commit()
            i += 1
