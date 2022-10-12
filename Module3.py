#Python Module: Module3


from datetime import date,datetime,timedelta
import mysql.connector



def DeleteRecord():
    try:
        mydb=mysql.connector.connect(host="localhost",user="root",password="root",database="Payroll")
        mycursor=mydb.cursor()
        eno=int(input("Enter Employee Number to be Deleted: "))
        sql="delete from EmployeeDetails where empno=%s"
        val=(eno,)
        mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        print("Records Deleted Successfully..........")

    except Exception as ex:
        print(ex)
        
    mydb.close()
