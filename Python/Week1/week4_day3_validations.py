#1.Count vowels

? 

cnt = 0
txt = ('a','e','i','o','u')

a = 'they are outside ' #  6

for i in a:
    if i in txt:
        cnt += 1
print(cnt)

#2.Count commas

?
a = 'the,y, ar,e outside '
x = a.count(',')
print(x)

#3.Check if salary is numeric

?

a = '11111'
x = a.isdigit()
print(x)

#4.Check if customer name contains only letters

?
a = 'aaa'
x = a.isalpha()
print(x)

#5.Find position of '@'
a = 'a@a'
x = a.find('@')
print(x)

#6.ETL Mini Exercise
#
# Use yesterday's customer file.
#C01,Ravi,ravi@gmail.com,25000,IT
C02,Arun,aa,35000,Finance
F03,John,john@gmail.com,9000,HR
C04,David,david@gmail.com,45000,sales
#C05,David,david@gmail.com,450a00,sales
#C06,David,david@gmail.com,45000,sales
# Implement three validations:
#
# Validation 1
#
# Customer ID should start with
# 
# C
# Validation 2
#
# Email should contain
#
# @
# Validation 3
#
# Salary should contain only digits.
#
# Hint:
#
# salary.isdigit()
#
# Expected Output
#
# Valid Customers
#
# C001 Ravi
#
# C002 Arun
#
# ------------------------
#
# Invalid Customers
#
# C004
#
# Reason : Invalid Email
#
# ------------------------
#
# C008
#
# Reason : Invalid Salary
#
# Do not worry about making it perfect. Focus on the logic.#

def validate_cust_id():
    with open('Customer1.txt') as f:
        X = f.readlines()
        reason_reject = []
        reason_accept = []

        for i in X:
            i = i.split(',')
            #print(i)
            cust_id = i[0]
            cust_name = i[1]
            cust_email = i[2]
            cust_salary = i[3]
          #  print(cust_email )
          #  print(cust_id)
          #  print(cust_email.find('@'))
          #  print (cust_id.startswith('C'))
            if cust_id.startswith('C') == True and cust_email.find('@') > 0 and cust_salary.isdigit() == True:
                #print(cust_id)
                reason_accept.append(
                            {
                                "Customer id":cust_id,
                                "Customer name":cust_name,
                                "Reason": "Valid Customers"
                            }
                            )
            elif cust_id.startswith('C') == False and cust_email.find('@') > 0 and cust_salary.isdigit() == True:
                reason_reject.append(
                    {
                        "Customer id": cust_id,
                        "Customer name": cust_name,
                        "Reason": "InValid Customer id"
                    }
                )
            elif cust_id.startswith('C') == True and cust_email.find('@') < 0 and cust_salary.isdigit() == True:
                reason_reject.append(
                    {
                        "Customer id": cust_id,
                        "Customer name": cust_name,
                        "Reason": "InValid Email"
                    }
                )

            elif cust_id.startswith('C') == True and cust_email.find('@') > 0 and cust_salary.isdigit() == False:
                reason_reject.append(
                    {
                        "Customer id": cust_id,
                        "Customer name": cust_name,
                        "Reason": "InValid Salary"
                    }
                )
        # print(reason_accept)
        # print(reason_reject)

    return (reason_accept,reason_reject)

reason_accept,reason_reject = validate_cust_id()
print('Valid Customers')
for i in reason_accept:
    #print(i)
    #print(type(i))
    print(i.get("Customer id"),i.get("Customer name"))
print('------------------------')

print('InValid Customers')
for i in reason_reject:
    # print(i)
    # print(type(i))
    print(i.get("Customer id"))
    print('Reason : ' + i.get("Reason"))
    print('------------------------')