
#Python Module: MyDatabase


from datetime import date,datetime,timedelta
import mysql.connector



def CreateDatabase():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root")
              mycursor=mydb.cursor()
              print("Creating Payroll Database")
              sql="create database if not exists Payroll"
              mycursor.execute(sql)
              print("Payroll Database Created Successfully....")
              
       except Exception as ex:
              print(ex)
       


def CreateRelations():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
              mycursor=mydb.cursor()
              print("Creating EmployeeDetails Relation")
              sql="create table if not exists EmployeeDetails(empno int primary key,ename varchar(50) not null,job varchar(50) not null,basicsalary int,DA float,HRA float,grosssalary float,tax float,netsalary float)"
              mycursor.execute(sql)
              print("EmployeeDetails Relation Created Successfully....")

       except Exception as ex:
              print(ex)


def ShowRelations():
       try:
              
              mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
              mycursor=mydb.cursor()
              print("Displaying List of Relations")
              sql="show tables"
              mycursor.execute(sql)
              for i in mycursor:
                     print(i)
               
       except Exception as ex:
              print(ex)

       




