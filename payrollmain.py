

#Python Module:Payroll Management


import Module1
import Module2
import Module3
import Module4
import Module5
import Module6
import Module7



while True:
    print("\t\t******Payroll Management******\n")
    print("==========================================")
    print("1. Adding Employee Records")
    print("2. For Displaying Record of All the Employees")
    print("3. For Deleting Record of a particular Employee")
    print("4. For Updation in a Record")
    print("5. For Searching a Record")
    print("6. For Displaying Salary Slip for all the Employees")
    print("7. Database Setup")
    print("8. Exit")
    print("==========================================")
    choice=int(input("Enter choice between 1 to 8 -------> :"))
    if choice==1:
        Module1.AddRecord()
    elif choice==2:
        Module2.DisplayAllRecord()
    elif choice==3:
        Module3.DeleteRecord()
    elif choice==4:
        Module4.UpdateRecord()
    elif choice==5:
        Module5.SearchRecord()
    elif choice==6:
        Module6.DisplaySalarySlip()
    elif choice==7:
        Module7.DataBase()
    elif choice==8:
        break
    else:
        print("Wrong choice.......Enter your choice again")
        x=input("enter any key to continue")
