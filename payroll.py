import payroll_database as db
while True:
    print('''choose the operation to perform:
    1.Adding Employee record
    2.Displaying Record Of All Employees
    3.For Displaying Record of Particular Employee
    4.For Deleting Record of Particular Employee
    5.For Modification In Record
    6.For Exit
    ''')

    
    choice = int(input('Enter Your Choice: '))
    if choice == 6:
        break
    elif choice==1:
            print('Enter Employee Information...')
            mempno=int(input('Enter Employee Number: '))
            mname=input('Enter Employee Name: ')
            mjob=input('Enter Employee Job: ')
            mbasic=float(input('Enter Basic Salary: '))
 
            mda=mbasic*0.48
            mhra=mbasic*0.25
            mtax=mbasic*0.1
            mgross=mbasic+mda+mhra
            mnet=mgross-mtax
            feedback=db.addEmployee(mempno,mname,mjob,mbasic,mda,mhra,mgross,mtax,mnet)
            print(feedback)
            
    elif choice==2:
        data=db.readall()
        for i in data:
            print((f'empno: {i[0]}\tname: {i[1]}\tjob: {i[2]}\tbasicsalary: {i[3]}\tDA: {i[4]}\tHRA: {i[5]}\tGrossSalary: {i[6]}\tTax: {i[7]}\tNetSalary: {i[8]}'))
       
    elif choice==3:
        empno=int(input('enter empno to be searched'))
        data=db.searchEmployee(empno)
        print((f'empno: {data[0]}\tname: {data[1]}\tjob: {data[2]}\tbasicsalary: {data[3]}\tDA: {data[4]}\tHRA: {data[5]}\tGrossSalary: {data[6]}\tTax: {data[7]}\tNetSalary: {data[8]}'))
        
    elif choice == 4:
        empno = int(input('Enter the empno to delete record: '))
        feedback = db.deleterecord(empno)
        print(feedback)
        
    elif choice == 5:
        empno = int(input('Enter the empno of employee to be update: '))
        data = list(db.searchEmployee(empno))

        print('''What do you want to update?
                1. name
                2. job
                3. basicSalary
                ''')
        upchoice = int(input('Enter Your Choice: '))
        if upchoice==1:
            name = input('Enter New name: ')
            data[1] = name
        elif upchoice==2:
            job = input('Enter New Job: ')
            data[2] = job
        elif upchoice==3:
            basicsalary = float(input('Enter New Salary: '))
            data[3] = basicsalary
            data[6] = basicsalary + data[4] + data[5]
            data[8] = data[6]-data[7]
            
        
        feedback = db.updaterecord(data)
        print(feedback)