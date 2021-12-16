import hashlib

import csv


class Person:
    
    def __init__(self,username,password,type):
        self.username = username
        self.password =password
        self.typeperson = typeperson


class Admin(Person):

    def insert_information(self):
        print("admin insert informationsabout lessons.")

class Student(Person): 

    def choose_lesson(self):
        print("Student chooses lessons.")




def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For Sigining Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
       return getdetails()
    elif choice == 2:
       return checkdetails()
    else:
       raise TypeError

def getdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password_insert = str(input("Password: "))
    password_encode = hashlib.md5(password_insert.encode())
    password = str(password_encode)
    f = open("User_Data.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt",'w')
    info = info + " " +name + " " + password
    f.write(info)

def checkdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password1 = info[index]
        usr_password0 = hashlib.md5(usr_password1.encode())
        usr_password = str(usr_password0)
        if usr_password == password:
            return "Welcome Back, " + name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."

print(choices())