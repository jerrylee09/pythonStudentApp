from student import Student

students = []

class HighSchoolStudent(Student):
    school_name = "Patrick Henry Hight"

    def get_school_name(self):
        return 'This is a hight School student'

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + '-HS'