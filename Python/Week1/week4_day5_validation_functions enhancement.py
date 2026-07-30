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


def loadable_records(custid,custname,custemail,custsalary):
    invalid_cnt1 = 0
    valid_cnt1 = 0
    custid_cnt1 = 0
    custnm_cnt1 = 0
    email_cnt1 = 0
    sal_cnt1 = 0
    # print(custid,custname,custemail.find('@'),custsalary.isdigit)
    if custid != '' and custname != '' and custemail.find('@') > 0 and custsalary.isdigit() == True:
     #   print('custid')
        valid_cnt1 = 1
      #  print(valid_cnt1)
    else:
        invalid_cnt1 = 1

    if custid == '':
        custid_cnt1 = 1
    elif custname == '':
        custnm_cnt1 = 1
    elif custemail.find('@') < 0:
        email_cnt1 = 1
    elif custsalary.isdigit() == False:
        sal_cnt1 = 1





    return valid_cnt1, invalid_cnt1,custid_cnt1,custnm_cnt1,email_cnt1,sal_cnt1

with open('Customer1.txt') as f:
    x = f.readlines()
    print('Total Records ' + str(len(x)))

    invalid_cnt1 = 0
    valid_cnt1 = 0
    custid_cnt1 = 0
    custnm_cnt1 = 0
    email_cnt1 = 0
    sal_cnt1 = 0
    for i in x:
        i = i.split(',')

        op1, op2, op3 = validate_cust_id(i[0], i[1], i[2], i[3])
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


        v, inv,cinv,cnminv,eminv,salinv = loadable_records(i[0], i[1], i[2], i[3])
        valid_cnt1 += v
        invalid_cnt1 += inv
        custid_cnt1 += cinv
        custnm_cnt1 += cnminv
        email_cnt1 += eminv
        sal_cnt1 += salinv
    print('Valid Records ' + str(valid_cnt1))
    print('Invalid Records '+str(invalid_cnt1))
    print('Invalid IDs Count ' +str(custid_cnt1))
    print('Invalid Names Count  '+str(custnm_cnt1))
    print('Invalid Emails Count ' +str(email_cnt1))
    print('Invalid Salaries Count  ' + str(sal_cnt1))