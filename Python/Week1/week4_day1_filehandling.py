#1.Read an entire file.
with open("Customer1.txt") as f:
        print(f.read())

with open("Customer1.txt") as f:
        print(f.readlines())

#2. Read one line at a time.

with open("Customer1.txt") as f:
        print(f.readline())
        print(f.readline())
        print(f.readline())

with open("Customer1.txt") as f:
        print(f.readline(),end='')
        print(f.readline(),end='')
        print(f.readline())

#3. Count total records.

with open("Customer1.txt") as f:
        print(len(f.readlines()))

#4. Print only customer IDs.

with open("Customer1.txt") as f:
        print('customer id')
        x1 =  f.readlines()

        for i in x1:
             i = i.split(",")
             print(i[0])

#5. Print only customer names.

with open("Customer1.txt") as f:
        print('customer Names')
        x1 =  f.readlines()

        for i in x1:
             i = i.split(",")
             print(i[1])

#6. Print records where email is missing.


with open("Customer1.txt") as f:
        print('customer with missing email id's')
        x1 =  f.readlines()

        for i in x1:
             i = i.split(",")
             j = i[2]
             if j == '':
                 print(i)

#7.Mini execercise

with open("Customer1.txt") as f:
        x1 =  f.readlines()
        print('Cid','Cust Name','Department')
        for i in x1:
             i = i.split(",")
             output1 = i[0]
             output2 = i[1]
             output3 = i[4]
             print(output1,output2,output3,end='')
             # print(f"Cust id: {output1}",f"Cust name: {output2}",f"Dept: {output3}",end='')

#8.Divide by zero.(Exp handling)

a = int(input('enter 1st number '))
b = int(input('enter 2nd number '))
try:
    c = a / b
    print(c)
except:
    print('An error occured')
finally:
    c= a/a
    print(a,c)


#10.Invalid number input.(Exp handling)


try:
    a = int(input('enter 1st number '))
    print(a)
except:
    print('An error occured')
    a = 2
    b = 10 ** a
    print(b)
finally:
    print(a)
    print(b)

#11.File not found.
try:
    with open("Customer22221.txt") as f:
        print(f.read())
except:
    with open("Customer221.txt", "a") as f:
        f.write("Woopaaaaaas! I have created the content!")