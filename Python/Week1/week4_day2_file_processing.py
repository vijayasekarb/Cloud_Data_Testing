
#1.Remove leading/trailing spaces.

with open('Customer2.txt') as f:
    x = f.readline()
    print(repr(x))
    x = x.strip()
    print(x)
    x = f.readline()
    print(repr(x))
    x = x.strip()
    print(x)
    x = f.readline()
    x = x.strip()
    print(x)

#2.Replace spaces with underscore.

with open('Customer2.txt') as f:
    x = f.readline()
    x = x.replace(  ' ','_')
    print(x)
    x = f.readline()
    x = x.replace(  ' ','_')
    print(x)
    x = x.replace(  ' ','_')
    print(x)

#3.Check if a customer ID starts with "C".

with open('Customer1.txt') as f:
    x = f.readlines()
    for i in x:
        i = i.split(',')
        i = (i[0])
        if i.startswith('C') is True:
            print(i,' Valid Customer')
        else:
            print(i, 'InValid Customer')

#4.Check if an email ends with .com.


with open('Customer1.txt') as f:
    x = f.readlines()
    for i in x:
        i = i.split(',')
        y = (i[0])
        i = (i[2])
        if i.endswith('.com') is True:
            print(y,i,' Valid email')
        else:
            print(y,i, 'InValid email')

#5.Convert department names to uppercase.

with open('Customer1.txt') as f:
    x = f.readlines()
    for i in x:
        i = i.split(',')
        i = (i[4])
        print(i.upper())

#6.Convert user input to lowercase before comparison.


ui = input('enter user input ')
with open('Customer1.txt') as f:
    x = f.readlines()
    for i in x:
        i = i.split(',')
        j = (i[4])
        if ui.lower() == j:
            print(i)

#7.ETL File Processing.

with open("Customer1.txt") as f:
    x1 = f.readlines()
    print('Cid', 'Cust Name', 'Department')
    for i in x1:
        i = i.split(",")
        output1 = i[0]
        output2 = i[1]
        output3 = i[4]
        #print(output1, output2, output3, end='')
        print(f"Cust id: {output1}",f"Cust name: {output2}",f"Dept: {output3}",end='')

#8.ETL Mini Exercise.(Not correct)


def validate_email_id():
    a2 = []
    a3 = ''
    with open('Customer1.txt') as f:
        x = f.readlines()
        for i in x:
            i = i.split(',')
            custid = (i[0])
            custname = (i[1])
            email = (i[2])
            if email != '':
                 a2.append(
                {
                    "Customer id": "Cust_id",
                    "Customer name": "Customer_Name",
                    "Reason": "valid Email Id"
                }
            )
        print(a2)

a1 = validate_email_id()

print(a1)


