import sys

class Data_error(Exception):
    pass
dict_student = {}
def update():

    l = {}
    id = int(input("enter student id"))

    if id not in dict_student.keys():
        try :
            id = id
            l["Name"] = input("Enter student name")
            l["Age"] = int(input("enter age"))
            n = list(map(int,input("enter marks separated in space").split()))
            l["Marks"] = n
            l["Total"] = sum(n)
            l["Avg"] = (sum(n)/len(n))
            dict_student[id] = l
            print("student data updated successfully")
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except:
            print("!!!!!!!!Enter valid  Marks!!!!!!!!!!")
def search():
    id = int(input("Enter Id of student"))
    try :
        if id in dict_student.keys():
            value = dict_student[id]
            for k in value:
                print(k,":",value[k])
        else:
            raise Data_error("")
    except Data_error:
        print("Data Doesn't Exist")
def delete():
    id = int(input("Enter Id of student"))
    if id in dict_student:
        dict_student.pop(id)
        print("Student data deleted Successfully")
    else:
        print("ID Does not Exist")
t = 1
while(t):
    try:
        op = int(input("!!!!Welcome!!!!\n1.Update\n2. Search\n3. Delete\n4. Exit\n"))
        if(op == 1):
            update()
        elif(op == 2):
            search()
        elif(op == 3):
            delete()
        elif(op == 4):
            sys.exit()
    except:
        print("Oops!!!Its not a number...")
