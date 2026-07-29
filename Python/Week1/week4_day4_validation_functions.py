def validate_salary(salary):
    #print(salary)
    if salary.isdigit() == True:
        print(salary.isdigit())
        op = salary.isdigit()
    else:
        op= salary.isdigit()
        print(op)
        return op

with open('Customer1.txt') as f:
    X = f.readlines()
    print ('Salary')
    for i in X:
            i = i.split(',')
            validate_salary(i[3])


def validate_cust_id(custid,custname,custemail,custsalary):
    op1 = None
    op2 = None
    op3 = None

   # print(custid)
    if custid != '' and custname != '' and custemail.find('@') > 0 and custsalary.isdigit() == True:
        print(custid)
        op1 = 'customer : ' + custid
        op2 = 'Status   : Valid'
        op3 = 'Reason   : Valid Record'
     #   print(op1)
    elif  custid == '' and custname != '' and custemail.find('@') > 0 and custsalary.isdigit() == True:
        op1 = 'customer : ' + custid
        op2 = 'Status   : In Valid'
        op3 = 'Reason   : Invalid cust id'
    elif custid != '' and custname == '' and custemail.find('@') > 0 and custsalary.isdigit() == True:
        op1 = 'customer : ' + custid
        op2 = 'Status   : In Valid'
        op3 = 'Reason   : Invalid Name'
       # print(op1)


    return op1,op2,op3

def validate_salary(custid,custname,custemail,custsalary):
    op1 = None
    op2 = None
    op3 = None

   # print(custid)
    if custsalary.isdigit() == False:
        print(custid)
        op1 = 'customer : ' + custid
        op2 = 'Status   : In Valid'
        op3 = 'Reason   : Invalid Salary'
     #   print(op1)
    return op1,op2,op3

def validate_email(custid,custname,custemail,custsalary):
    op1 = None
    op2 = None
    op3 = None

   # print(custid)
    if custemail.find('@') < 0 :
        print(custid)
        op1 = 'customer : ' + custid
        op2 = 'Status   : In Valid'
        op3 = 'Reason   : Invalid email'
     #   print(op1)
    return op1,op2,op3

with open('Customer1.txt') as f:
    X = f.readlines()

    for i in X:
            i = i.split(',')
            #print(i)
            op1, op2, op3 = validate_cust_id(i[0],i[1],i[2],i[3])
            if op1 is not None:
                print(op1)
                print(op2)
                print(op3)
            op1, op2, op3 = validate_salary(i[0], i[1], i[2], i[3])
            if op1 is not None:
                print(op1)
                print(op2)
                print(op3)
            op1, op2, op3 = validate_email(i[0], i[1], i[2], i[3])
            if op1 is not None:
                    print(op1)
                    print(op2)
                    print(op3)