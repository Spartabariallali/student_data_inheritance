from student_data import Student_name

class Devops_student(Student_name):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print(self.first_name, " ", self.last_name)

    def roll_call(self):
        print("I am a Devops Student")

    
student_two = Devops_student("bari","allali")
student_two.full_name()
student_two.roll_call()