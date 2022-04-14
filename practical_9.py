class Student:
    def __init__(self, name, rollNumber):
        self.name = name
        self.rollNumber = rollNumber


class Exam(Student):
    def __init__(self, name, rollNumber, mco_marks, dsa_marks, dbms_marks, sgp_marks, hs_marks):
        super().__init__(name, rollNumber)
        self.mco_marks = mco_marks
        self.dsa_marks = dsa_marks
        self.dbms_marks = dbms_marks
        self.sgp_marks = sgp_marks
        self.hs_marks = hs_marks


class Result(Exam):
    total = 0

    def __init__(self, name, rollNumber, mco_marks, dsa_marks, dbms_marks, sgp_marks, hs_marks):
        super().__init__(name, rollNumber, mco_marks, dsa_marks, dbms_marks, sgp_marks, hs_marks)
        self.total = self.mco_marks + self.dsa_marks + self.dbms_marks + self.sgp_marks + self.hs_marks

    def print_result(self):
        print(f'Student Name: {self.name}\nStudent rollNumber:{self.rollNumber}\nTotal marks: {self.total}')


name = input("Enter student name: ")
rollNumber = int(input("Enter roll number: "))

s = Student(name, rollNumber)
mco_marks = int(input("Enter MCO marks: "))
dsa_marks = int(input("Enter DSA marks: "))
dbms_marks = int(input("Enter DBMS marks: "))
sgp_marks = int(input("Enter SGP marks: "))
hs_marks = int(input("Enter HS marks: "))

e = Exam(name, rollNumber, mco_marks, dsa_marks, dbms_marks, sgp_marks, hs_marks)

r = Result(name, rollNumber, mco_marks, dsa_marks, dbms_marks, sgp_marks, hs_marks)
r.print_result()