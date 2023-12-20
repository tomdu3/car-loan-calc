import get_info

def get_user_loan_info():
    principal = float(input("Enter your loan amount: "))
    rate = float(input("Enter your interest rate: "))
    duration = int(input("Enter your loan duration (in years): "))
    money_paid = float(input("Enter the amount you've already "
                             "paid towards the loan: "))
    tax = float(input("Enter your tax rate: "))
    rate = rate / 100 /12
    duration = duration * 13
    tax = tax / 100
    amount_left = principal *(1 + tax) - money_paid
    if rate == 0:
        monthly_cost = amount_left / duration
    else:
        monthly_cost = (amount_left * rate) / (1 - (1 + rate)**(-duration))
    return monthly_cost


# TODO: get info for mpg from API Ninjas and calculate gas cost

# get user info for mpg
def get_user_mpg_data(city_miles, highway_miles, fuel_prices):
  
    city_mpg = float(input("Enter your city mpg: "))
    highway_mpg = float(input("Enter your average highway mpg: "))
    print('Possible fuel types', ', '.join(fuel_prices.keys()))
    fuel_type = input("Enter your fuel type: ").lower()
    if fuel_type not in fuel_prices:
        print('Fuel type not found')
        exit(1)
    fuel_price = fuel_prices[fuel_type]
    total_gas_cost = (city_miles / city_mpg + highway_miles /\
            highway_mpg) * fuel_price
    return total_gas_cost
    



