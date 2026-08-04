# ETL Validation Framework
#
# Version: 0.7
# Status: Code Cleanup
# Author: Vijaya Sekar Balan

# Features:
#
# CSV Validation
# Modular Validation
# Valid Record Collection
# Invalid Record Collection
# Multiple Error Detection
# Summary Generation
# Report Generation
# Exception Handling
def customer_file_validation():
    INPUT_FILE = "customer.csv"

#Identify valid records
    def is_valid_record(custid, custname, custemail, custsalary,):
        if custid != '' and custname != '' and '@' in custemail and custsalary.isdigit():
            is_valid = True
            return is_valid

# collect only  valid records
    def collect_valid(custid,is_valid):

        if is_valid:
            valid_list.append(
            {
                "Customer id": custid,
                "Status": 'Valid'
            }
            )
        return valid_list

#Validate customer id
    def validate_cust_id(custid, custname, custemail, custsalary):
        op1 = None
        op2 = None
        op3 = None
        if custid == '':
            op1 = custid
            op2 = 'In Valid'
            op3 = 'Invalid cust id'
        return op1, op2, op3

# Validate customer name
    def validate_cust_name(custid, custname, custemail, custsalary):
        op1 = None
        op2 = None
        op3 = None
        if custname == '':
            op1 = custid
            op2 = 'In Valid'
            op3 = 'Invalid cust name'
        return op1, op2, op3

# Validate salary
    def validate_salary(custid, custname, custemail, custsalary):
        op1 = None
        op2 = None
        op3 = None
        if not custsalary.isdigit():
            op1 = custid
            op2 = 'In Valid'
            op3 = 'Invalid Salary'
        return op1, op2, op3

# Validate email
    def validate_email(custid, custname, custemail, custsalary):
        op1 = None
        op2 = None
        op3 = None
        if '@' not in custemail:
            op1 = custid
            op2 = 'In Valid'
            op3 = 'Invalid email'
        return op1, op2, op3

#Prepare count summary
    def loadable_records(custid, custname, custemail, custsalary,is_valid):
        invalid_cnt1 = 0
        valid_cnt1 = 0
        custid_cnt1 = 0
        custnm_cnt1 = 0
        email_cnt1 = 0
        sal_cnt1 = 0
        if is_valid:
            valid_cnt1 = 1
        else:
            invalid_cnt1 = 1
        if custid == '':
            custid_cnt1 = 1
        if custname == '':
            custnm_cnt1 = 1
        if '@' not in custemail:
            email_cnt1 = 1
        if not custsalary.isdigit():
            sal_cnt1 = 1
        return valid_cnt1, invalid_cnt1, custid_cnt1, custnm_cnt1, email_cnt1, sal_cnt1

#Collect invalid record

    def collect_error(op1, op2, op3):
        if op1 is not None:
            error_list.append(
                {
                    "Customer id": op1,
                    "Status": op2,
                    "Reason": op3
                }
            )
#Print the summary of report

    def print_summary():
        prev_rec = 'a'
        for i in valid_list:
          if i != []:
              print('Customer : ' + i.get("Customer id"))
              print('Status :' + i.get("Status"))
        for i in error_list:
            if i != []:
                if prev_rec != i.get("Customer id"):
                    print('Customer :',i.get("Customer id"))
                    print('Status :', i.get("Status"))
                    print('Reason :', i.get("Reason"))
                    prev_rec = i.get("Customer id")
                else:
                    print('Reason :', i.get("Reason"))

#Main program to call and open the files

    import csv

    try:
        with open(INPUT_FILE) as f:


            f_reader = csv.reader(f)
            invalid_cnt1 = 0
            valid_cnt1 = 0
            custid_cnt1 = 0
            custnm_cnt1 = 0
            email_cnt1 = 0
            sal_cnt1 = 0
            cnt1 = 0
            error_list = []
            valid_list = []
            next(f_reader)


#looping into records and calling each validation functions

            for i in f_reader:

                is_valid = is_valid_record(i[0], i[1], i[2], i[3])

                valid_list = collect_valid(i[0],is_valid)

                cnt1 += 1

                op1, op2, op3 = validate_cust_id(i[0], i[1], i[2], i[3])
                collect_error(op1, op2, op3)

                op1, op2, op3 = validate_cust_name(i[0], i[1], i[2], i[3])
                collect_error(op1, op2, op3)

                op1, op2, op3 = validate_salary(i[0], i[1], i[2], i[3])
                collect_error(op1, op2, op3)

                op1, op2, op3 = validate_email(i[0], i[1], i[2], i[3])
                collect_error(op1, op2, op3)

                v, inv, cinv, cnminv, eminv, salinv = loadable_records(i[0], i[1], i[2], i[3],is_valid)
                valid_cnt1 += v
                invalid_cnt1 += inv
                custid_cnt1 += cinv
                custnm_cnt1 += cnminv
                email_cnt1 += eminv
                sal_cnt1 += salinv

            print_summary()

            print('Total Records ' + str(valid_cnt1+invalid_cnt1))
            print('Valid Records ' + str(valid_cnt1))
            print('Invalid Records '+str(invalid_cnt1))
            print('Invalid IDs Count ' +str(custid_cnt1))
            print('Invalid Names Count  '+str(custnm_cnt1))
            print('Invalid Emails Count ' +str(email_cnt1))
            print('Invalid Salaries Count  ' + str(sal_cnt1))

            summary = {
                    'Total Records ': str(valid_cnt1+invalid_cnt1),
                    'Valid Records ': str(valid_cnt1),
                    'Invalid Records ': str(invalid_cnt1),
                    'Invalid IDs Count ': str(custid_cnt1),
                    'Invalid Names Count  ': str(custnm_cnt1),
                    'Invalid Emails Count ': str(email_cnt1),
                    'Invalid Salaries Count ': str(sal_cnt1),
                  }



            return valid_list,error_list,summary

    except FileNotFoundError:
        print(f"ERROR : Input file '{INPUT_FILE}' not found.")
        print("Validation aborted.")
        return [],[],{}




valid_list, error_list, summary  = customer_file_validation()

#Write the saummary in to the .txt file
def write_report(valid_list,error_list,summary):
    OUTPUT_FILE = "ETL_Validation.txt"

    with open(OUTPUT_FILE,'w') as f:

        f.write('***************' + "\n")
        f.write('Valid Customers'+ "\n")
        f.write('***************' + "\n")

        prev_rec = 'a'

        for i in valid_list:
            f.write('Customer : '+i.get("Customer id")+ "\n")
            f.write('Status : '+i.get("Status") + "\n")

        f.write('***************' + "\n")
        f.write('InValid Customers' + "\n")
        f.write('***************' + "\n")

        for i in error_list:
            if prev_rec != i.get("Customer id"):
               f.write('Customer : ' + i.get("Customer id") + "\n")
               f.write('Status : ' + i.get("Status") + "\n")
               f.write('Reason : ' + i.get("Reason") + "\n")
               prev_rec = i.get("Customer id")
            else:
               f.write('Reason : ' + i.get("Reason") + "\n")

        f.write('***************' + "\n")
        f.write('Summary' + "\n")
        f.write('***************' + "\n")


        f.write('Total Records '+summary['Total Records ']+ "\n")
        f.write('Valid Records '+summary['Valid Records ']+ "\n")
        f.write('Invalid IDs Count ' + summary['Invalid IDs Count ']+ "\n")
        f.write('Invalid Names Count  ' + summary['Invalid Names Count  ']+ "\n")
        f.write('Invalid Emails Count ' + summary['Invalid Emails Count ']+ "\n")
        f.write('Invalid Salaries Count ' + summary['Invalid Salaries Count '])

if summary:
    write_report(valid_list,error_list,summary)