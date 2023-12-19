import requests
import json
import dotenv
import os

# Load the environment variables

if os.path.isfile('.env'):
    dotenv.load_dotenv()
    print('Environment variables loaded')
## remove the following lines if deploying to heroku
else:
    print('Environment variables not loaded')
    os.exit(1)

# set the API key and URL
RAPID_API_KEY = os.getenv('RAPID_API_KEY')
RAPID_URL = 'https://gas-price.p.rapidapi.com/allUsaPrice'
NINJA_API_KEY = os.getenv('NINJA_API_KEY')
NINJA_URL = 'https://api.api-ninjas.com/v1/cars'


# Get the fuel data from the RAPID API
def get_fuel_us():
    fuel_headers = {
        'X-RapidAPI-Key': RAPID_API_KEY,
        'X-RapidAPI-Host': 'gas-price.p.rapidapi.com'
    }
    response = requests.get(RAPID_URL, headers=fuel_headers)
    if response.status_code == 200:
        print('Data retrieved successfully')
        with open('fuel_data.json', 'w') as f:
            json.dump(response.json(), f)
    else:
        print('Error retrieving data')
        print(response.status_code)
        print(response.text)
        os.exit(1)

def get_fuel_cost():

    if os.path.isfile('fuel_data.json'):
        update_cost = input('Would you like to update the fuel cost data? (y/n) ')
        if update_cost.lower() == 'y':
            get_fuel_us()
    else:
        get_fuel_us()

    with open('fuel_data.json', 'r') as f:
        fuel_data = json.load(f)

    # check if data was retrieved successfully
    if not fuel_data['success']:
        print('Error retrieving data')
        os.exit(1)
    
    states = {state['name']: id for id, state in enumerate(fuel_data['result'])}
    print(states)

    # get the state and return the gas price
    state = input("Enter your state: ").capitalize()
    if state in states:
        state_id = states[state]
        return {
                'state': state,
                'gasoline': fuel_data['result'][state_id]['gasoline'],
                'midGrade': fuel_data['result'][state_id]['midGrade'],
                'premium': fuel_data['result'][state_id]['premium'],
                'diesel': fuel_data['result'][state_id]['diesel']
            }
    else:
        print('State not found')
        os.exit(1)

def show_fuel_cost(fuel):
    print("---- Fuel Information ----")
    print("--------------------------")
    
    for key in fuel:
        print(key + ": " + str(fuel[key]))


# def retrieve_mpg_data(mpg):
#    mpg_headers = {
#        'X-Api-Key': NINJA_API_KEY
#    }
#    mpg_params = {
#        'make': mpg['make'],
#        'model': mpg['model'],
#        'year': mpg['year']
#    }
#    response = requests.get(NINJA_URL, headers=mpg_headers, params=mpg_params)
#    if response.status_code == 200:
#        print('Data retrieved successfully')
#        with open('mpg_data.json', 'w') as f:
#            json.dump(response.json(), f)
#        print(response.json())
#        return response.json()
#    else:
#        print('Error retrieving data')
#        print(response.status_code)
#        print(response.text)
#        os.exit(1)

def get_user_stats():
    print("---- User Information ----")
    print("--------------------------")
    user_stats = {}
    user_stats['city_weekday_miles'] = float(input('Enter your average work week city miles: '))
    user_stats['city_weekend_miles'] = float(input('Enter your average weekend city miles: '))
    user_stats['highway_weekday_miles'] = float(input('Enter your average work week highway miles: '))
    user_stats['highway_weekend_miles'] = float(input('Enter your average weekend highway miles: '))
    user_stats['city_month_miles'] = user_stats['city_weekday_miles'] * 4 + user_stats['city_weekend_miles'] * 4
    user_stats['highway_month_miles'] = user_stats['highway_weekday_miles'] * 4 + user_stats['highway_weekend_miles'] *4
    user_stats['monthly_miles'] = user_stats['city_month_miles'] + user_stats['highway_month_miles']
    return user_stats

def show_user_stats(user_stats):
    print("---- User Information ----")
    print("--------------------------")
    for key in user_stats:
        print(key + ": " + str(user_stats[key]))
