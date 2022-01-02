import json
def sign_up():
    email = input("Enter email address: ")
    db = open("./crud/crud.json","r")
    if email in db.read():
            print("please login")
    else:
        db = open("./crud/crud.json","r")
        dic=json.loads(db.read())
        print(dic)
        user_name = input("Enter user name: ")
        password = input("create password: ")

        
        flag = False
        flag1 = strong_password(password)
        
        print(flag1)
        if flag1 == True:
            password2 = input("confirm password: ")
            if password == password2:
                gender = input("Enter gender: ")
                gender1= ["MALE","FEMALE","TRANSGENDER"]
                if gender.upper() in gender1:
                    dob = input("Enter date of birth: ")
                    print("you can access")
                    dic.update({email: [user_name,password,gender,dob]})
                    
                    db=open("./crud/crud.json","w")

                    json.dump(dic,db)

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
            print("enter minimum 1 capital and 1 small and  1 number 1 special character from #,@,$,*")

def delete():
    email = input("enter email address:")


def login():
    db = open("crud.json","r")
    email = input("Enter email address: ")
    password = input("enter password: ")
    if password in db.read():
        print("you can access")
    elif email in db.read():
        print("you can access")
    else:
        print("please signup")
        sign_up()
option = input("1.login\n2.signup\n3.update\n4.delete\nenter your choice:")
if option == "1" :
    login()
elif option == "2":
    sign_up()
# elif option == "3":
#     update()
# elif option == "4":
#     delete()
else:
    print("correct option")
