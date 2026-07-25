"""
Mini Project - Version 2

Topics Used:
- Variables
- If-Else
- Loops
- Dictionaries
- Lists
- Functions
- Return Statements

Purpose:
Validate customer records and generate business-friendly summary and rejection report.

Version:
2.0
"""

input1 = [{'Cust_id' : 'C01','Customer_Name' : 'Çust1' ,'Email' :'Çust1@','Dept' : 'HR','Salary':1000},
          {'Cust_id' : 'C02','Customer_Name' : 'Çust2' ,'Email' :'Çust2@' ,'Dept' : 'Finance','Salary':10000},
          {'Cust_id' : '',   'Customer_Name' : 'Çust3' ,'Email' :'Çust3@' ,'Dept' : 'HR','Salary':10000},
	      {'Cust_id' : 'C04','Customer_Name' : '' ,'Email' :'Çust4@','Dept' : 'IT','Salary':10000},
	      {'Cust_id' : '','Customer_Name' : 'Çust5' ,'Email' :'Çust5','Dept' : 'Sales','Salary':1000},
	      {'Cust_id' : 'C06','Customer_Name' : '' ,'Email' :'Çust6','Dept' : 'XXX','Salary':10000},
	      {'Cust_id' : 'C07','Customer_Name' : 'Çust7' ,'Email' :'Çust7@','Dept' : 'HR','Salary':100},
	      {'Cust_id' : '',   'Customer_Name' : '' ,'Email' :'Çust8','Dept' : 'HR','Salary':1000},
	      {'Cust_id' : 'C09','Customer_Name' : 'Çust9' ,'Email' :'Çust9','Dept' : 'XX','Salary':100},
	      {'Cust_id' : 'C10','Customer_Name' : 'Cust10' ,'Email' :'Çust10@','Dept' : 'IT','Salary':10000}]

total_cust = ('Total customer is '+str(len(input1)))
def validate_cust_id():
    invalid_cnt1 = 0
    valid_cnt1 = 0
    reason_rejection = []
    for i in input1:
        cust_id_len = len(i.get("Cust_id"))
        cust_name_len = len(i.get("Customer_Name"))
        #print((len(i.get("Cust_id"))))
        if cust_id_len != 0 and cust_name_len !=0 :
            valid_cnt1 += 1
        else:
            invalid_cnt1 += 1
            reason_rejection.append(
                {
                    "Customer id":i.get("Cust_id"),
                    "Customer name": i.get("Customer_Name"),
                    "Reason": "Invalid Cust id or name"
                }
                )

    return valid_cnt1, invalid_cnt1,reason_rejection

def validate_email_id():
    invalid_cnt1 = 0
    valid_cnt1 = 0
    reason_rejection = []
    for i in input1:
        email_id_find = i.get("Email")
        email_id_find = email_id_find.find('@')
        if email_id_find >-1:
            valid_cnt1 += 1
        else:
            invalid_cnt1 += 1
            reason_rejection.append(
                {
                    "Customer id": i.get("Cust_id"),
                    "Customer name": i.get("Customer_Name"),
                    "Reason": "Invalid Email Id"
                }
            )
    return valid_cnt1, invalid_cnt1,reason_rejection


def validate_department():
        invalid_cnt1 = 0
        valid_cnt1 = 0
        reason_rejection = []
        str1 = ('HR', 'Finance', 'Sales', 'IT')
        for i in input1:
            dept_find = i.get("Dept")
            if dept_find in str1:
                valid_cnt1 += 1
            else:
                invalid_cnt1 += 1
                reason_rejection.append(
                    {
                        "Customer id": i.get("Cust_id"),
                        "Customer name": i.get("Customer_Name"),
                        "Reason": "Invalid deperment"
                    }
                )
        return valid_cnt1, invalid_cnt1,reason_rejection

def validate_salary():
    invalid_cnt1 = 0
    valid_cnt1 = 0
    reason_rejection = []
    for i in input1:
        salary_crt = i.get("Salary")
        if salary_crt == 10000:
            valid_cnt1 += 1
        else:
            invalid_cnt1 += 1
            reason_rejection.append(
                {
                    "Customer id": i.get("Cust_id"),
                    "Customer name": i.get("Customer_Name"),
                    "Reason": "Invalid Salary"
                }
            )
    return valid_cnt1, invalid_cnt1,reason_rejection

def loadable_records():
    invalid_cnt1 = 0
    valid_cnt1 = 0
    str1 = ('HR', 'Finance', 'Sales', 'IT')
    for i in input1:
        cust_id_len = len(i.get("Cust_id"))
        cust_name_len = len(i.get("Customer_Name"))
        email_id_find = i.get("Email")
        email_id_find = email_id_find.find('@')
        dept_find = i.get("Dept")
        salary_crt = i.get("Salary")
        if cust_id_len != 0 and cust_name_len !=0 and email_id_find >-1 and dept_find in str1 and salary_crt == 10000:
            valid_cnt1 += 1
        else:
            invalid_cnt1 += 1

    return valid_cnt1, invalid_cnt1

def generate_summary():

    print(total_cust)

    valid_cnt1,invalid_cnt1,reason_rejection = validate_cust_id()
    print('##############Customer id / name validation summary#######################')
    print ('No of customer with Valid customer id and name is '+str(valid_cnt1))
    print ('No of customer with Invalid customer id and name is ' + str(invalid_cnt1))
    print('=================================================')
    print ('Customer_id','customer_name','Reason')
    print('=================================================')
    #print(reason_rejection)
    for i in reason_rejection:
       # print(i.get("Customer id"))
       # print(i.get("Customer name"))
        if i.get("Customer id") == '' and i.get("Customer name") != '':
            print('           ',i.get("Customer name"),'        '+i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") == '':
            print(i.get("Customer id"),'             ','        '+i.get("Reason"))
            y = '     '
        elif i.get("Customer id") == '' and i.get("Customer name") == '':
            print('            ','            ',i.get("Reason"))

    print('=================================================')

    valid_cnt1, invalid_cnt1, reason_rejection = validate_email_id()
    print('##############Customer Email id validation summary#######################')
    print('No of customer with Valid Email id is ' + str(valid_cnt1))
    print('No of customer with Invalid Email id is ' + str(invalid_cnt1))
    print('===========================================')
    print('Customer_id', 'customer_name', 'Reason')
    print('===========================================')
    #print(reason_rejection)
    for i in reason_rejection:
        # print(i.get("Customer id"))
        # print(i.get("Customer name"))
        if i.get("Customer id") == '' and i.get("Customer name") != '':
            print('           ', i.get("Customer name"),'        '+ i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") == '':
            print(i.get("Customer id"), '                     ', i.get("Reason"))
            y = '     '
        elif i.get("Customer id") == '' and i.get("Customer name") == '':
            print('          ','              ',i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") != '':
            print(i.get("Customer id"),'        '+i.get("Customer name"), '        '+i.get("Reason"))

    print('===========================================')

    print('=================================================')

    valid_cnt1, invalid_cnt1, reason_rejection = validate_department()
    print('##############Customer department validation summary#######################')
    print('No of customer with valid Department is ' + str(valid_cnt1))
    print('No of customer with Invalid Department is ' + str(invalid_cnt1))
    print('===========================================')
    print('Customer_id', 'customer_name', 'Reason')
    print('===========================================')
    # print(reason_rejection)
    for i in reason_rejection:
        # print(i.get("Customer id"))
        # print(i.get("Customer name"))
        if i.get("Customer id") == '' and i.get("Customer name") != '':
            print('           ', i.get("Customer name"), '        ' + i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") == '':
            print(i.get("Customer id"), '                     ', i.get("Reason"))
            y = '     '
        elif i.get("Customer id") == '' and i.get("Customer name") == '':
            print('          ', '              ', i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") != '':
            print(i.get("Customer id"), '        ' + i.get("Customer name"), '        ' + i.get("Reason"))

    print('===========================================')

    valid_cnt1, invalid_cnt1, reason_rejection = validate_salary()
    print('##############Customer department validation summary#######################')
    print('No of customer with valid Department is ' + str(valid_cnt1))
    print('No of customer with Invalid Department is ' + str(invalid_cnt1))
    print('===========================================')
    print('Customer_id', 'customer_name', 'Reason')
    print('===========================================')
    # print(reason_rejection)
    for i in reason_rejection:
        # print(i.get("Customer id"))
        # print(i.get("Customer name"))
        if i.get("Customer id") == '' and i.get("Customer name") != '':
            print('           ', i.get("Customer name"), '        ' + i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") == '':
            print(i.get("Customer id"), '                     ', i.get("Reason"))
            y = '     '
        elif i.get("Customer id") == '' and i.get("Customer name") == '':
            print('          ', '              ', i.get("Reason"))
        elif i.get("Customer id") != '' and i.get("Customer name") != '':
            print(i.get("Customer id"), '        ' + i.get("Customer name"), '        ' + i.get("Reason"))

    print('===========================================')

    valid_cnt1, invalid_cnt1 = loadable_records()
    print('No of Loadable records are ' + str(valid_cnt1))
    print('No of Rejectable records are  ' + str(invalid_cnt1))

    print('===========================================')

generate_summary()