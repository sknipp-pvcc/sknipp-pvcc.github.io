import datetime

hourly_rate = (16.50, 15.75, 15.75, 19.58)
deductions = (.12, .03, .062, .0145)
fed_tax = 0
state_tax = 0
ss_tax = 0
medicare_tax = 0
total_deductions = 0
net_pay = 0
job_cat = ""
hours = 0
pay_rate = 0

def get_employee_data():
    global hours, job_cat
    hours = int(input("How many hours has employee worked?:   "))
    job_cat = str(input("What is your job category? C: Cashier, J: Janitor, S: Stoker, M: Mainenance"))
    
def perform_calculations():
    global pay_rate, gross_pay, net_pay, total_deductions, fed_tax, state_tax, ss_tax, medicare_tax
    if job_cat == "Cashier" or job_cat.upper() == "C":
        gross_pay = hourly_rate[0] * hours
        pay_rate = hourly_rate[0]
    elif job_cat == "Stocker":
        gross_pay = hourly_rate[1] * hours
        pay_rate = hourly_rate[1]
        
    elif job_cat == "Janitor":
        gross_pay = hourly_rate[2] * hours
        pay_rate = hourly_rate[2]
    elif job_cat == "Maintenance":
        gross_pay = hourly_rate[3] * hours
        pay_rate = hourly_rate [3]
    
    total_deductions = (gross_pay * deductions[0]) + (gross_pay * deductions[1]) + (gross_pay * deductions[2]) + (gross_pay * deductions[3])
    fed_tax = gross_pay * deductions[0]
    state_tax = gross_pay * deductions[1]
    ss_tax = gross_pay * deductions[2]
    medicare_tax = gross_pay* deductions[3]
    net_pay = gross_pay - total_deductions
    
    
   

def paystub():
    print('-------------------------------')
    print('**Fresh Foods Employee Weekly Pay**')
    print('*******Employee Pay Stub*******')
    print('-------------------------------')
    print('Job Title        '+ job_cat)
    print('Pay Rate         $'+ format(pay_rate,'8,.2f'))
    print('Hours             '+ format(hours,'8,.2f'))
    print('Federal Tax      $'+ format(fed_tax,'8,.2f'))
    print('State Tax        $'+ format(state_tax,'8,.2f'))
    print('Social Security  $'+ format(ss_tax,'8,.2f'))
    print('Medicare         $'+ format(medicare_tax,'8,.2f'))
    print('Gross Pay        $'+ format(gross_pay,'8,.2f'))
    print('Total Deductions $'+ format(total_deductions,'8,.2f'))
    print('Net Pay          $'+ format(net_pay,'8,.2f'))
    print('-------------------------------')
    print(str(datetime.datetime.now()))
    print("Thank you for your business!")



def main():
    while True:
        get_employee_data()
        perform_calculations()
        paystub()
        option = str(input("Would you like an additional paystub for another employee? "))
        if option == "n" or option == "no" or option == "No":
            break

    
main()
