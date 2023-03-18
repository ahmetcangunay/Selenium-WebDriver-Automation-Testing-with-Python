class Student:

    __student_name = ""
    __student_surname = ""

    def __init__(self, name, surname):

        self.__student_name = name
        self.__student_surname = surname

    def get_name(self):
        return f"{self.__student_name} {self.__student_surname}"

    def set_name(self, name, surname):
        self.__student_name = name
        self.__student_surname = surname
