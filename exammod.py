import mysql.connector
from mysql.connector import Error
import os
import time

def home(uid):
    ans=True
    uname=FindUserName(uid);
    while ans:
        os.system('cls')
        print("                COMPUTER QUIZ")
        print("********************************************************")
        print("  Welcome ",uname)
        print("********************************************************")
        print("  1. Take Exam")
        print("  2. View Result")
        print("  3. View Profile")
        print("  4. Edit Profile")
        print("  5. Exit")
        print("********************************************************")
        ch=int(input("Enter Choice(1-5) :"))
        if ch==1: 
            subid = ChooseSubject(uname)
            startexam(subid,uname,uid)
            ThankYou(uname)
        elif ch==2:
            ShowResults(uid,uname)
        elif ch==3:
            ShowProfile(uid,uname)
        elif ch==4:
            EditProfile(uid,uname)
        elif ch==5:
            ans=False
        else:
            print("Invalid Choice")
        input("Enter any key to continue....")
def FindUserName(uid):
    uname=""
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from users_tb where userid='"+uid+"'")
    rows = cursor.fetchall()
    cursor.close()
    if len(rows)>0:
        uname = str(rows[0][2])
    return(uname)

def ChooseSubject(uname):
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  Welcome ",uname)
    print("********************************************************")
    print("  Choose Subject:")
    print("  1. C++")
    print("  2. Java")
    print("  3. Python")
    print("  4. C")
    print("********************************************************")
    ch=int(input("Enter Choice(1-4) :"))
    sid=""
    if ch==1:
        sid="sub001"
    elif ch==2:
        sid="sub002"
    elif ch==3:
        sid="sub003"
    elif ch==4:
        sid="sub004"
    return(sid)

def startexam(subid,uname,uid):
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from questions_tb where sid='"+subid+"'")
    rows = cursor.fetchall()
    subname=FindSubName(subid)
    ClearAnsTable()
    for i in range(0,len(rows)):
        os.system('cls')
        print("                COMPUTER QUIZ")
        print("****************************************************************************")
        print("  Welcome ",uname)
        print("*****************************************************")
        print("  Subject:",subname,"\tDate:",time.strftime("%d/%m/%Y"),"\tTime:",time.strftime("%I:%M:%S"))
        print("****************************************************************************")
        print("Q.",i+1," ",rows[i][1]);
        print("1.",rows[i][2])
        print("2.",rows[i][3])
        print("3.",rows[i][4])
        print("4.",rows[i][5])
        print("****************************************************************************")
        uans=int(input("Your Ans(1-4):"))
        ans=""
        if uans==1:
            ans=rows[i][2]
        elif uans==2:
            ans=rows[i][3]
        elif uans==3:
            ans=rows[i][4]
        elif uans==4:
            ans=rows[i][5]
        SaveUserAns(ans)
    CalculateResult(subid,uid)
    ClearAnsTable()
def FindSubName(subid):
    sname=""
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from subjects_tb where subid='"+subid+"'")
    rows = cursor.fetchall()
    cursor.close()
    if len(rows)>0:
        sname = str(rows[0][1])
    return(sname)

def ThankYou(uname):
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  Welcome ",uname)
    print("********************************************************")
    print()
    print("       Thank You, Your exam is over")
    print()
    print("********************************************************")
    input(" Press any key to continue.........")

def SaveUserAns(ans):
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("insert into tempans_tb values('"+ans+"')")
    conn.commit()
    cursor.close()

def ClearAnsTable():
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("delete from tempans_tb")
    conn.commit()
    cursor.close()

def CalculateResult(subid,uid):
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')

    cursor = conn.cursor()
    cursor.execute("select * from questions_tb where sid='"+subid+"'")
    row = cursor.fetchone()
    clist=[]
    while row is not None:
        clist.append(row[6])
        row = cursor.fetchone()

    cursor.execute("select * from tempans_tb")
    row = cursor.fetchone()
    ulist=[]
    while row is not None:
        ulist.append(row[0])
        row = cursor.fetchone()

    noq=len(clist)
    correct=0
    for i in range(0,len(clist)):
        if clist[i] == ulist[i]:
            correct+=1
    percent = int((correct/noq)*100)
    examid = CreateNewExamId()
    doe=time.strftime("%d/%m/%Y")

    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    query = "insert into results_tb values('"+examid+"','"+uid+"','"+subid+"','"+doe+"',"+str(noq)+","+str(correct)+","+str(percent)+")"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()

def CreateNewExamId():
    newid=""
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select examid from results_tb order by examid desc limit 1")
    rows = cursor.fetchall()
    cursor.close()
    if len(rows)>0:
        tempid = str(rows[0][0])
        n=tempid[3:]
        n=int(n)
        n+=1
        if n>0 and n<10:
            newid="exm00"+str(n)
        elif n>=10 and n<100:
            newid="exm0"+str(n)
        else:
            newid="exm"+str(n)
    else:
        newid="exm001"
    return(newid)

def ShowResults(uid,uname):
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from results_tb where uid='"+uid+"'")
    rows = cursor.fetchall()
    cursor.close()
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  Welcome ",uname)
    print("********************************************************")
    print("ExamId\tSubject\tExamDate\tPercentage")
    print("********************************************************")
    for i in range(0,len(rows)):
        sname=FindSubName(rows[i][2])
        print(rows[i][0],"\t",sname,"\t",rows[i][3],"\t",rows[i][6])
    print("********************************************************")
    input("Press any key to go back........")

def ShowProfile(uid,uname):
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  Welcome ",uname)
    print("********************************************************")
    print(" Your Profile is as follows:")
    print("********************************************************")
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from users_tb where userid='"+uid+"'")
    rows = cursor.fetchall()
    cursor.close()
    print("  User Id\t:",rows[0][0])
    print("  Password\t:",rows[0][1])
    print("  First Name\t:",rows[0][2])
    print("  Last Name\t:",rows[0][3])
    print("  Dob\t\t:",rows[0][4])
    print("  Gender\t:",rows[0][5])
    print("  Address\t:",rows[0][6])
    print("  Contact\t:",rows[0][7])
    print("  Email\t\t:",rows[0][8])
    print("********************************************************")
    input("Press any key to go back........")
def EditProfile(uid,uname):
    os.system('cls')
    print("                COMPUTER QUIZ")
    print("********************************************************")
    print("  Welcome ",uname)
    print("********************************************************")
    print(" Your Old Profile is as follows:")
    print("********************************************************")
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    cursor.execute("select * from users_tb where userid='"+uid+"'")
    rows = cursor.fetchall()
    cursor.close()
    print("  User Id\t:",rows[0][0])
    print("  Password\t:",rows[0][1])
    print("  First Name\t:",rows[0][2])
    print("  Last Name\t:",rows[0][3])
    print("  Dob\t\t:",rows[0][4])
    print("  Gender\t:",rows[0][5])
    print("  Address\t:",rows[0][6])
    print("  Contact\t:",rows[0][7])
    print("  Email\t\t:",rows[0][8])
    print("********************************************************")
    print("Enter Updated data:")
    password=input("  Password    :")
    fname=input("  First Name  :")
    lname=input("  Last Name   :")
    dob=input("  Dob         :")
    gender=input("  Gender(m/f) :")
    address=input("  Address     :")
    contact=input("  Contact     :")
    email=input("  Email       :")
    conn = mysql.connector.connect(host='localhost',database='examdb',user='root',password='')
    cursor = conn.cursor()
    query = "update users_tb set password='"+password+"',firstname='"+fname+"',lastname='"+lname+"',dob='"+dob+"',gender='"+gender+"',address='"+address+"',contact='"+contact+"',email='"+email+"' where userid='"+uid+"'"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    print("********************************************************")
    input("Press any key to go back........")
