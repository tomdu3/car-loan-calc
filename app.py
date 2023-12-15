import get_info
import calculator


def main():
    # get user info for fuel from RAPID API
    fuel = get_info.get_fuel_us()

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


if __name__ == '__main__':
    main()
