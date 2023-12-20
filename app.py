import get_info
import calculator
import scrape_maintenance

def main():
    # get user info for fuel from RAPID API
    fuel = get_info.get_fuel_cost()
    state = fuel['state']
    fuel_prices = {
        'gasoline': float(fuel['gasoline']),
        'midgrade': float(fuel['midGrade']),
        'premium': float(fuel['premium']),
        'diesel': float(fuel['diesel'])
    }
   
    # get user stats
    user_stats = get_info.get_user_stats()
    city_miles = user_stats['city_month_miles']
    highway_miles = user_stats['highway_month_miles']

    # get user info for mpg from API Ninjas
    # mpg = calculator.get_user_mpg_info()
    # calculator.show_mpg_info(mpg)


    # get user info for maintenance cost
    maintenance_monthly_cost = scrape_maintenance.get_maintenance_cost()

 
    # get car info from user
    number_of_cars = int(input("How many cars do you wish to check for? "))
    cars = {}
    print('------ Enter car details -------')
    print('--------------------------------')
    print('Available brands:', ', '.join(maintenance_monthly_cost.keys()))
    cars = []
    for i in range(number_of_cars):
        car = {}
        car['brand'] = input("Enter your car make: ").capitalize()
        if car['brand'] not in maintenance_monthly_cost:
            print('Brand not found')
            exit(1)
        car['maintenance_monthly_cost'] =maintenance_monthly_cost[car['brand']]
        car['monthly_gas_cost'] = calculator.get_user_mpg_data(
                city_miles, highway_miles, fuel_prices)
        car['loan_monthly_cost'] = calculator.get_user_loan_info()
        car['total_monthly_cost'] = car['maintenance_monthly_cost'] + \
                car['monthly_gas_cost'] + car['loan_monthly_cost']
        cars.append(car)
    print('--------------------------------')
    print('------ Car monthly costs -------')
    for car in cars:
        print('Brand: ' + car['brand'])
        print('Maintenance cost: ' + str(car['maintenance_monthly_cost']))
        print('Gas cost: ' + str(car['monthly_gas_cost']))
        print('Loan cost: ' + str(car['loan_monthly_cost']))
        print('--------------------------------')
        print('Total monthly cost: ' + str(car['total_monthly_cost']))
        print('--------------------------------')


if __name__ == '__main__':
    main()
