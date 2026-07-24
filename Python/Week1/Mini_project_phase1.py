
input1 = [{'Cust_id' : 'C01','Customer_Name' : 'Çust1' ,'Email' :'Çust1@','Dept' : 'HR','Salary':10000},
          {'Cust_id' : 'C02','Customer_Name' : 'Çust2' ,'Email' :'Çust2@' ,'Dept' : 'Finance','Salary':10000},
          {'Cust_id' : '',   'Customer_Name' : 'Çust3' ,'Email' :'Çust3@' ,'Dept' : 'HR','Salary':10000},
	      {'Cust_id' : 'C04','Customer_Name' : '' ,'Email' :'Çust4@','Dept' : 'IT','Salary':10000},
	      {'Cust_id' : 'C05','Customer_Name' : 'Çust5' ,'Email' :'Çust5','Dept' : 'Sales','Salary':10000},
	      {'Cust_id' : 'C06','Customer_Name' : 'Çust6' ,'Email' :'Çust6@','Dept' : 'XXX','Salary':10000},
	      {'Cust_id' : 'C07','Customer_Name' : 'Çust7' ,'Email' :'Çust7@','Dept' : 'HR','Salary':100},
	      {'Cust_id' : '',   'Customer_Name' : 'Çust8' ,'Email' :'Çust8','Dept' : 'HR','Salary':10000},
	      {'Cust_id' : 'C09','Customer_Name' : 'Çust9' ,'Email' :'Çust9','Dept' : 'XX','Salary':100},
	      {'Cust_id' : 'C10','Customer_Name' : 'Cust10' ,'Email' :'Çust10@','Dept' : 'IT','Salary':10000}]

total_cust = ('Total customer is '+str(len(input1)))
print (total_cust)
def validate_cust_id():
    invalid_cnt1 = 0
    valid_cnt1 = 0
    for i in input1:
        cust_id_len = len(i.get("Cust_id"))
        cust_name_len = len(i.get("Customer_Name"))
        #print((len(i.get("Cust_id"))))
        if cust_id_len != 0 and cust_name_len !=0 :
            valid_cnt1 += 1
        else:
            invalid_cnt1 += 1
    print('No of customer with Valid customer id and name is '+str(valid_cnt1))
    print('No of customer with Invalid customer id and name is ' + str(invalid_cnt1))
def validate_email_id():
    invalid_cnt1 = 0
    valid_cnt1 = 0

    for i in input1:
        email_id_find = i.get("Email")
        email_id_find = email_id_find.find('@')
        if email_id_find >-1:
            valid_cnt1 += 1
        else:
            invalid_cnt1 += 1
    print('No of Valid email id is '+str(valid_cnt1))
    print('No of Invalid email id is ' + str(invalid_cnt1))

def validate_department():
        invalid_cnt1 = 0
        valid_cnt1 = 0
        str1 = ('HR','Finance','Sales','IT')
        for i in input1:
            dept_find = i.get("Dept")
            if dept_find in str1:
                valid_cnt1 += 1
            else:
                invalid_cnt1 += 1
        print('No of employees having Valid deptarment is ' + str(valid_cnt1))
        print('No of employees having Invalid deptarment is  ' + str(invalid_cnt1))
def validate_salary():
        invalid_cnt1 = 0
        valid_cnt1 = 0
        for i in input1:
            salary_crt = i.get("Salary")
            if salary_crt == 10000:
                valid_cnt1 += 1
            else:
                invalid_cnt1 += 1
        print('No of employees having Valid salary is ' + str(valid_cnt1))
        print('No of employees having Invalid salary is  ' + str(invalid_cnt1))
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
    print('No of Loadable records are ' + str(valid_cnt1))
    print('No of Rejectable records are  ' + str(invalid_cnt1))

validate_cust_id()
validate_email_id()
validate_department()
validate_salary()
loadable_records()

##############################Below is the o/p of the program

C:\Users\vijayudhaya\PycharmProjects\Cloud_Data_Testing\venv\Scripts\python.exe C:\Users\vijayudhaya\PycharmProjects\Cloud_Data_Testing\main.py 
Total customer is 10
No of customer with Valid customer id and name is 7
No of customer with Invalid customer id and name is 3
No of Valid email id is 7
No of Invalid email id is 3
No of employees having Valid deptarment is 8
No of employees having Invalid deptarment is  2
No of employees having Valid salary is 8
No of employees having Invalid salary is  2
No of Loadable records are 3
No of Rejectable records are  7

