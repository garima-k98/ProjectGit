class Student:
    def __init__(self,name,sem,rollno):
        self.name=name
        self.semester=sem
        self.rollno=rollno
    def display(self):
        return f" The student name is {self.name},"\
            f" branch is {self.semester} and rollno is {self.rollno}."
class CSE(Student):
    def display(self):
        return f" The CSE student name is {self.name},"\
            f" semester is {self.semester} and rollno is {self.rollno}."

s1=Student("Garima",3,12345)
s2=CSE("karoosh",7,45678)
print(s1.display())
print(s2.display())
