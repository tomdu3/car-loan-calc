import get_info
import calculator
import scrape_maintenance

def main():
    # get user info for fuel from RAPID API
    fuel = get_info.get_fuel_cost()
    get_info.show_fuel_cost(fuel)

    # get user info for mpg from API Ninjas
    mpg = calculator.get_user_mpg_info()
    calculator.show_mpg_info(mpg)

    # show loan info
    loan = calculator.get_user_loan_info()
    calculator.show_loan_info(loan)

    # calculate loan monthly cost
    monthly_cost = calculator.calculate_loan_monthly_cost(loan)
    # show loan monthly cost
    print("Your monthly cost is: " + str(monthly_cost))

    # get user info for maintenance cost
    maintenance_cost = scrape_maintenance.get_maintenance_cost()
    scrape_maintenance.show_maintenance_cost(maintenance_cost)
    
if __name__ == '__main__':
    main()
