Week3-Day-6

#Program 1

 Accept Employee Name, Experience and Salary.

Print:

Fresher
Mid-Level
Senior

based on experience.

empname = input('Enter employee name ')
empexp  = int(input('Enter employee exp '))
empsal  = int(input('Enter employee sal '))

if empexp < 3:
    print('Fresher')
elif empexp >= 3 and empexp < 10:
    print('Mid Level')
else:
    print('Senior')

#Program 2 

Check Loan Eligibility

Conditions:

Salary > 50000
Experience > 5
Existing Loan = No

Otherwise reject.

empsal = int(input('Enter employee salary '))
empexp = int(input('Enter employee exp '))
existloan = input('Do you have existing Loan ?')
existloan = existloan.upper()

#Program 3

 Student Grade

Use multiple if-elif.

engmark = int(input('Enter English mark '))
mathmark = int(input('Enter Math mark '))
scimark = int(input('Enter Sci mark '))
attempt = int(input('Which attemp ?  '))

average = (engmark+mathmark+scimark)/3

if attempt ==1 and  average > 90:
    print('Grade A')
elif attempt == 2 and  average > 90:
    print('Grade B')
elif attempt > 2 and average > 90:
    print('Grade C')
else:
    print('Grade D')

#Program 4

Print numbers

1–100

Only multiples of 5.

for i in range(1,101):
    x = i % 5
    if x == 0:
        print(i)

#Program 5

Print all even numbers

between

50–100.

for i in range(50,101):
    x = i % 2
    if x == 0:
        print(i)

#Program 6

Count

How many numbers between

1–100

are divisible by

3 and 5.

ctr1 = 0
ctr2 = 0

for i in range(1,101):
    x = i % 3
    if x == 0:
        ctr1 += 1
print(ctr1)
for i in range(1,101):
    x = i % 5
    if x == 0:
        ctr2 += 1
print(ctr2)

#Program 7

Store

10 employee names

inside a List.

Print them.

employee_names = ['A','B','C']
for i in employee_names:
    print(i)
print(type(employee_names))

#Program 8

Store

10 Department names

inside a Set.

Print unique departments.
dept_names = {'A','B','a','C','C'}
for i in dept_names:
    print(i)
print(type(dept_names))

#Program 9Create Dictionary

Employee

ID

Name

Salary

Department

Print all Keys.

Print all Values.

Loop through Dictionary

emp_det = {'empid' :'E1','empname' : 'VIJAY','salary' : 1000 }
print(emp_det.keys())
print(emp_det.values())
for i in emp_det:
    print(emp_det.items())


#Program 10Create

validate_salary()

Return

Eligible

Not Eligible


def validate_salary():
    salary1 = int(input('Enter Salary '))
    
    if salary1 >= 1000:
        print('Eligible')
    else:
        print('Not Eligible')

validate_salary()

#Program 11

Create

calculate_bonus()

Bonus Rules:

60000 ? 15%

40000–60000 ?10%

<40000 ?5%


def calculate_bonus():
    salary1 = int(input('Enter Salary '))
    if salary1 >= 60000:
       bonus = (salary1*15)/100
    elif salary1 >= 40000 and salary1 < 60000:
       bonus = (salary1 * 10) / 100
    elif salary1 < 40000:
        bonus = (salary1 * 5) / 100
    print(bonus)

calculate_bonus()

#Program 12

Create

validate_email()

Simply check whether

'@'

exists.

(No advanced validation yet.)

def validat_email():
    email1 = input('Enter email ')

    if email1.find('@') < 0:
        print('Invalid Email')
    else:
        print('Valid Email')
validat_email()