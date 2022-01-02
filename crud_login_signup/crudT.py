import json
def sign_up():
    email = input("Enter email address: ")
    db = open("./crud_login_signup/crud.json","r")
    if email in db.read():
            print("please login")
    else:
        db = open("./crud_login_signup/crud.json","r")
        ctr = 0
        for i in db.read():
            ctr+=1
        if ctr == 0:
            dic={}
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
                        dob = input("Enter date of birth: ")
                        print("you can access")
                        dic.update({email: [user_name,password,gender,dob]})
                        db=open("./crud_login_signup/crud.json","a")
                        json.dump(dic,db,indent=4)
                    else:
                        print("correct gender")
            
                else:
                    print("password did not match")
        else:
            db = open("./crud_login_signup/crud.json","r")
            dic=json.loads(db.read())
            print(dic)
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
                        dob = input("Enter date of birth: ")
                        print("you can access")
                        dic.update({email: [user_name,password,gender,dob]})
                        db=open("./crud_login_signup/crud.json","w")
                        json.dump(dic,db,indent=4)
                    else:
                        print("correct gender")
                else:
                    print("password did not match")
def strong_password(password):
    special_character = ["#","@","$","*"]
    if len(password) < 8:
        print("enter more than 8 character")
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
            print("enter minimum 1 spec")
            print("l=",l,"u=",u,"s=",s,"d=",d)

def delete():
    email = input("enter email address:")
    db = open("./crud_login_signup/crud.json","r")
    dic= json.loads(db.read())
    dic.pop(email)
    db = open("./crud_login_signup/crud.json","w")
    json.dump(dic,db,indent=5)
    db.close()
def login():
    db = open("./crud_login_signup/crud.json","r")
    ctr = 0
    email = input("Enter email address: ")
    password = input("enter password: ")
    

    for i in db.read():
        ctr+=1
    if ctr == 0:
        print("please signup")
        sign_up()
    else:
        db = open("./crud_login_signup/crud.json","r")
        x = json.loads(db.read())
        if email in x.keys():
            if password in x[email]:
                print("you can access")
        else:
            print("please signup")
            sign_up()
def update():
    email = input("enter your email id: ")
    user_name = input("enter new username: ")
    password =input("enter new password: ")
    flag1 = strong_password(password)
    if flag1 == True:
        password2 = input("confirm password: ")
        if password == password2:
            gender = input("Enter gender: ")
            gender1= ["MALE","FEMALE","TRANSGENDER"]
            if gender.upper() in gender1:
                dob = input("Enter date of birth: ")
                db = open("./crud_login_signup/crud.json","r")
                dic = json.loads(db.read())
                db.close()
                db = open("./crud_login_signup/crud.json","w")
                dic.update({email: [user_name,password,gender,dob]})
                json.dump(dic,db,indent=4)
                print("your detail is updated.")
                db.close()
            else:
                print("correct gender")
        else:
            print("password did not match")
    # gender = input("Enter gender: ")
    # gender1= ["MALE","FEMALE","TRANSGENDER"]
    # if gender.upper() in gender1:
    #     dob = input("enter new date of birth: ")
    #     db = open("./crud_login_signup/crud.json","r")
    #     dic = json.loads(db.read())
    #     db.close()
    #     db = open("./crud_login_signup/crud.json","w")
    #     dic.update({email: [user_name,password,gender,dob]})
    #     json.dump(dic,db,indent=4)
    #     print("your detail is updated.")
    #     db.close()
    # else:
    #     print("correct gender")
option = input("1.login\n2.signup\n3.update\n4.delete\nenter your choice:")
if option == "1" :
    login()
elif option == "2":
    sign_up()
elif option == "3":
    update()
elif option == "4":
    delete()
else:
    print("Enter correct option")
