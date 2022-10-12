#Python Module: Module5


from datetime import date,datetime,timedelta
import mysql.connector

def SearchRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        eno=int(input("Enter Employee Number to be Searched: "))
        sql="select * from EmployeeDetails where empno=%s"
        val=(eno,)
        mycursor.execute(sql,val)
        rcount=0
        for (empno,ename,job,basicsalary,DA,HRA,grosssalary,tax,netsalary) in mycursor:
            rcount+=1
            print("==============================================")
            print("==============================================")
            print("Employee No: ",empno)
            print("Employee Name: ",ename)
            print("Employee Job: ",job)
            print("Basic Salary: ",basicsalary)
            print("DA: ",DA)
            print("HRA: ",HRA)
            print("Gross Salary: ",grosssalary)
            print("Tax:",tax)
            print("Net Salary:",netsalary)
            print("===============================================")
        if rcount%2==0:
            print(rcount,"Record(s)  not found")
        
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Searched Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()

