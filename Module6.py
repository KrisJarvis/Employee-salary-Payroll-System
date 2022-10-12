#Python Module: Module6


import datetime
import mysql.connector

def DisplaySalarySlip():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        sql="select * from EmployeeDetails"
        mycursor.execute(sql)
        now=datetime.datetime.now()
        print("\n\n\n\t\t\tSALARY SLIP ")
        print("Current Date and Time: ",end=" ")
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        for (empno,ename,job,basicsalary,DA,HRA,grosssalary,tax,netsalary) in mycursor:
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
                
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Searched Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()
