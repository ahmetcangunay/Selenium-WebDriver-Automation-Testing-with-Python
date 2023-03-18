import homework_1_Student as stu
import homework_1_StudentDao as dao

student1 = stu.Student("Ahmet Can", "GÜNAY")

student_dao = dao.StudentDao()

student_dao.create_table("student_list.db")

# student_dao.add_student("Ahmet Can", "GÜNAY")

student_dao.get_all_students()

# student_dao.delete_student("Ahmet Can", "GÜNAY")

student_list = [("Berker", "SARI"), ("Ali", "OSMAN"), ("Mete", "GEZMİŞ")]

student_dao.add_multiple_student(student_list)

student_dao.get_all_students()

student_dao.get_student_number_by_name("Ali")
