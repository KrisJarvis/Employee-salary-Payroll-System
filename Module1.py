#Python Module: Module1


from datetime import date,datetime,timedelta
import mysql.connector



def AddRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        print("Enter Employee information......")
        eno=int(input("Enter Employee No: "))
        ename=input("Enter Employee Name: ")
        ejob=input("Enter Employee Job: ")
        ebasic=float(input("Enter Basic Salary: "))
        if ejob.upper()=="OFFICER":
            eda=ebasic*0.5
            ehra=ebasic*0.35
            etax=ebasic*0.2
        elif ejob.upper()=="MANAGER":
            eda=ebasic*0.45
            ehra=ebasic*0.30
            etax=ebasic*0.15
        else:
            eda=ebasic*0.40
            ehra=ebasic*0.25
            etax=ebasic*0.1

        egross=ebasic+eda+ehra+etax
        enet=egross-etax
        #rec=(eno,ename,ejob,ebasic,eda,ehra,egross,etax,enet)
            
        sql="insert into EmployeeDetails values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val=(eno,ename,ejob,ebasic,eda,ehra,egross,etax,enet)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Inserted Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()
