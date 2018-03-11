students = []

class Student:
    # static varible
    school_name = "Patrick Henry"
    def __init__ (self, name, student_id = 1):
        self.name = name
        self.student = student_id
        students.append(self)

    def __str__(self):
        return 'Student ' + self.name

    def get_name_capitalize(self):
        return self.name.captialize(self)

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "Patrick Henry Hight"

    def get_school_name(self):
        return 'This is a hight School student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + '-HS'

    # this is the constructor method
    # def __init__(self, name, student_id=1):
    #     student = {"name": name, "student_id": student_id}
    #     students.append(student)
    #     # self.add_student(student)
    #
    # #  str is a method override
    # def __str__(self):
    #     return "student"

    #pass # interpreter to do nothing
    # def add_student(self, name, student_id=1):
    #     student = {"name": name, "student_id": student_id}
    #     students.append(student)
    #     # self.add_student(student)

jerry = HighSchoolStudent('Jerry')
print(jerry)
# print(Student.school_name) # this can be call because school name is not an instance. It is a class attribute
# student.add_student('Jerry') # only need to be called of it is not contructor




# student = Student() # new intances of the class
#
# print(student)
#
# new_student = Student() # new intances of the class
#
# print(new_student)