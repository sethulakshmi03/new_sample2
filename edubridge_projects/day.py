import sys
dict_student = {}

def update():

    l = []
    id = int(input("enter student id"))
    if id not in dict_student.keys():
        l.append(input("Enter student name"))
        l.append(int(input("enter age")))
        n = list(map(int,input("enter marks separated in space").split()))
        l.append(n)
        l.append(sum(n))
        l.append((sum(n)/len(n)))
        dict_student[id] = l
        print("student data updated successfully")
    else:
        print("Id already existed")

def search():
    id = int(input("Enter Id of student"))
    if id in dict_student.keys():
        value = dict_student[id]
        print("Name:",value[0])
        print("Age:", value[1])
        print("Marks:", value[2])
        print("Sum:", value[3])
        print("Avg:", value[4])

    else:
        print("ID Does not Exist")
def delete():
    id = int(input("Enter Id of student"))
    if id in dict_student:
        dict_student.pop(id)
        print("Student data deleted Successfully")
    else:
        print("ID Does not Exist")
t = 1
while(t):
    op = int(input("!!!!Welcome!!!!\n1.Update\n2. Search\n3. Delete\n4. Exit\n"))
    if(op == 1):
        update()
    elif(op == 2):
        search()
    elif(op == 3):
        delete()
    elif(op == 4):
        sys.exit()
