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



# students = []
#
#
# class Student:
#
# 	school_name = "Springfield Elementary"
#
# 	def __init__(self, name, student_id=332):
# 		self.name = name
# 		self.student_id = student_id
# 		students.append(self)
#
# 	def __str__(self):
# 		return "Student " + self.name
#
# 	def get_name_capitalize(self):
# 		return self.name.capitalize()
#
# 	def get_school_name(self):
# 		return self.school_name