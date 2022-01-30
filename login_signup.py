from curses.ascii import isspace
import json
import os
from re import sub
# print(os.getcwd())
####sign_up function
def sign_up():
    email = input("Enter email address: ")
    email_validity(email)
    db = open("./crud.json","r")
    x= (db.read())
    db.close()
    if email in x:
        json_data =json.loads(x)
        if email in json_data.keys():
            print("plese login")
    else:
        json_data =json.loads(x)
        sub_dic_sign ={"user_name":"","password":"","gender":"","dob":""}
        user_name = input("Enter user name: ")
        password = input("create password: ")
        flag = False
        flag1 = strong_password(password)
        if flag1 == True:
            password2 = input("confirm password: ")
            if password == password2:
                gender = input("Enter gender: ")
                gender1= ["MALE","FEMALE","TRANSGENDER"]
                if gender.upper() in gender1:
                    dob = input("Enter date of birth : ")
                    print("plese login.")
                    sub_dic_sign["user_name"]=user_name;sub_dic_sign["password"]=password;sub_dic_sign["gender"]=gender;sub_dic_sign["dob"]=dob
                    json_data.update({email: sub_dic_sign})
                    db=open("./crud.json","w")
                    json.dump(json_data,db)
                else:
                    print("correct gender")
            else:
                print("password did not match")
def strong_password(password):
    special_character = ["#","@","$","*"]
    if len(password) < 8:
        print("enter more than 8 character")
        exit()
    else:
        l,u,s,d=0,0,0,0
        for i in password:
            if i.isupper():
                u+=1
            elif i.islower():
                l+=1
            elif i.isdigit():
                d+=1
                s+=1
        if l>=1 and u>=1 and d>=1 and s>=1:
            global flag
            flag = True
            return flag
        else:
            print("enter minimum 1 capital and 1 small and  1 number 1 special character from #,@,$,*")
            exit()

def delete():
    email = input("Enter email address: ")
    email_validity(email)
    db = open("./crud.json","r")
    x= (db.read())
    db.close()
    if email in x:
        json_data =json.loads(x)
        if email in json_data.keys():
            print("chose option\n1.delete account")
            user_choice = input("enter choice: ")
            if user_choice=="1":
                del(json_data[email])
                print(json_data)
                db= open("./crud.json","w")
                json.dump(json_data,db,indent=5)
                db.close()
        else:
            print("Plese sign_up")
    else:
        print("Plese sign_up")
####email  validity
def email_validity(email):
    if "@gmail.com" in email:
        pass
    elif ".org" in email:
        pass
    else:
        print("enter correct email address.")
        exit()
#login function
def login():
    db = open("crud.json","r")
    email = input("Enter email address: ")
    email_validity(email)
    password = input("enter password: ")
    if password in db.read():
        print("you can access")
    elif email in db.read():
        print("you can access")
    else:
        print("you are not logged in.\nplease signup")
        sign_up()
option = input("1.login\n2.signup\n3.update\n4.delete\nenter your choice:")
def update():
    email = input("Enter email address: ")
    password = input("Enter your password: ")
    email_validity(email)
    db = open("./crud.json","r")
    x= (db.read())
    if email in x:
        json_data =json.loads(x)
        if password in json_data[email].values():
            if email in json_data.keys():
                for i in json_data.values():
                    for j in i:
                        user_name = input("update user name: ")
                        password = input("update password: ")
                        strong_password(password)
                        gender = input("Enter gender: ")
                        gender1= ["MALE","FEMALE","TRANSGENDER"]
                        if gender.upper() in gender1:
                            dob = input("Enter date of birth : ")
                            print("your detail is updated.")
                            json_data[email]["user_name"]=user_name;json_data[email]["password"]=password;
                            json_data[email]["gender"]=gender;json_data[email]["dob"]=dob;
                            db=open("./crud.json","w")
                            json.dump(json_data,db,indent=5)
                            db.close()
                            print(json_data)
                            exit()
        else:
            print("plese signup.")
#user choice
if option == "1" :
    login()
elif option == "2":
    sign_up()
elif option == "3":
    update()
elif option == "4":
    delete()
else:
    print("Plese enter correct option")