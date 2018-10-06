import mysql.connector
from mysql.connector import Error
import os

def register():
    newuserid = createnewuserid()
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  REGISTER USER")
    print("")
    print("  User Id     :",newuserid)
    password=input("  Password    :")
    fname=input("  First Name  :")
    lname=input("  Last Name   :")
    dob=input("  Dob         :")
    gender=input("  Gender(m/f) :")
    address=input("  Address     :")
    contact=input("  Contact     :")
    email=input("  Email       :")
    print("********************************************************")
    input("Press any key to save and go back......")
    query = "insert into users_tb values('"+newuserid+"','"+password+"','"+fname+"','"+lname+"','"+dob+"','"+gender+"','"+address+"','"+contact+"','"+email+"')"
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
def createnewuserid():
    newid=""
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select userid from users_tb order by userid desc limit 1")
    rows = cursor.fetchall()
    cursor.close()
    if len(rows)>0:
        tempid = str(rows[0][0])
        n=tempid[3:]
        n=int(n)
        n+=1
        if n>0 and n<10:
            newid="usr00"+str(n)
        elif n>=10 and n<100:
            newid="usr0"+str(n)
        else:
            newid="usr"+str(n)
    else:
        newid="usr001"
    return(newid)

def login():
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  LOGIN USER")
    print("")
    uid =input("  User Id     :")
    password=input("  Password    :")

    usid=""
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from users_tb where userid='"+uid+"' and password='"+password+"'")
    rows = cursor.fetchall()
    cursor.close()
    if len(rows)>0:
        usid=uid
    else:
        input("Invalid Login Credentials")
    return(usid)
