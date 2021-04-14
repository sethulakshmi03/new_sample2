import re
import sys

class Data_error(Exception):
    pass
dict_student = {1:{"Name":"Sethu","Age":30,"Address":"valasaravakkam chennai","Phone_number":123456789,"Marks":[12,23,45],"Total":100,"Avg":100},
                2:{"Name":"Sandeep","Age":36,"Address":"valasaravakkam chennai","Phone_number":123456785,"Marks":[32,23,55],"Total":200,"Avg":200},
                3:{"Name":"sabu","Age":56,"Address":"cherthala alappuzha","Phone_number":147258369,"Marks":[52,93,55],"Total":300,"Avg":300},
                4:{"Name":"Seetha","Age":32,"Address":"ponnukkara thrissur","Phone_number":741852963,"Marks":[72,93,85],"Total":400,"Avg":400}}
def update():

    l = {}
    id = int(input("enter student id"))

    if id not in dict_student.keys():
        try :
            id = id
            l["Name"] = input("Enter student name")
            l["Age"] = int(input("enter age"))
            l["Address"] = input("Enter Your Address separated in space")
            l["Phone_number"] = input("Enter your phone number")
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

    p = int(input("Enter 1. Search using Id 2. Address "))
    if p == 1:
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
    elif p == 2:
        ad = input("Enter address")

        for k,v in dict_student.items():
            res = re.findall(ad,v["Address"])
            if len(res) >= 1:
                print("#######################################")
                for key,val in v.items():
                    print(key,':',val)
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
