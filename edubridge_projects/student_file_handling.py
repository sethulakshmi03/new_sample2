r = open("Student_file","a+")
r.write("ID Name Age Address Marks Average Total")
class student_data:
    def __init__(self):
    def update(self,op,id):

        name = input("Enetr name of the Student")
        age = int(input("Enetr age"))
        address = input("Enetr Student Address")
        marks = map(int,input("Enetr marks separated in space").split())
        avg = sum(marks)/len(avg)
        total = sum(marks)
    def insert(self):
        Id = int(input("Enter Your ID"))
        name = input("Enetr name of the Student")
        age = int(input("Enetr age"))
        address = input("Enetr Student Address")
        marks = map(int, input("Enetr marks separated in space").split())
        avg = sum(marks) / len(avg)
        total = sum(marks)
        str = "{0} {1} {2} {3} {4} {5} {6}"
    def read(self):
    def delet(self):
