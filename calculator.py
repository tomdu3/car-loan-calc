import get_info

def get_user_loan_info():
    loan = {}
    loan['principal'] = float(input("Enter your loan amount: "))
    loan['rate'] = float(input("Enter your interest rate: "))
    loan['duration'] = float(input("Enter your loan duration (in years): "))
    loan['money paid'] = float(input("Enter the amount you've already paid towards the loan: "))
    loan['tax'] = float(input("Enter your tax rate: "))
    return loan

def show_loan_info(loan):
    print("---- Loan Information ----")
    print("--------------------------")
    for key, value in loan.items():
        print(key.title() + ": " + str(value))

def calculate_loan_monthly_cost(loan):
    principal = loan['principal']
    rate = loan['rate'] / 100 /12
    duration = loan['duration'] * 12
    money_paid = loan['money paid']
    tax = loan['tax'] / 100
    amount_left = principal *(1 + tax) - money_paid
    if rate == 0:
        monthly_cost = amount_left / duration
    else:
        monthly_cost = (amount_left * rate) / (1 - (1 + rate)**(-duration))
    return monthly_cost

# get user info info for mpg from API Ninjas
def get_user_mpg_info():
    mpg = {}
    mpg['make'] = input("Enter your car make: ")
    mpg['model'] = input("Enter your car model: ")
    mpg['year'] = input("Enter your car year: ")
    return mpg

def show_mpg_info(mpg):
    print("---- Mpg Information ----")
    print("--------------------------")
    mpg_data = get_info.retrieve_mpg_data(mpg)

    # print info table
    for item in mpg_data:
        print(item.title() + ": " + str(mpg_data[item]))

