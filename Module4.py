#Python Module: Module4


from datetime import date,datetime,timedelta
import mysql.connector


def UpdateRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        eno=int(input("Enter Employee Number to be Updated: "))
        sql="select * from EmployeeDetails where empno=%s"
        val=(eno,)
        print("Enter New Record")
        ename=input("Enter Employee Name: ")
        ejob=input("Enter Employee Job: ")
        ebasic=int(input("Enter Basic Salary: "))
        eda=float(input("Enter DA: "))
        ehra=float(input("Enter HRA: "))
        egrosssalary=int(input("Enter Gross Salary: "))
        etax=int(input("Enter Tax: "))
        enetsalary=int(input("Enter Net Salary: "))
        sql2="update EmployeeDetails set ename=%s,job=%s,basicsalary=%s where empno=%s"
        val2=(ename,ejob,ebasic,eno)
        mycursor.execute(sql2,val2)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Updated Successfully..........")

    except Exception as ex:
        print("Something went wrong",ex)
        
    mydb.close()

