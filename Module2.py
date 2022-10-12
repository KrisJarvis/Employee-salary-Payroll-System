#Python Module: Module2


from datetime import date,datetime,timedelta
import mysql.connector




def DisplayAllRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        sql="select * from EmployeeDetails"
        mycursor.execute(sql)
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

    except Exception as ex:
        print("Spmething went wrong",ex)
        
    mydb.close()
