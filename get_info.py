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

# get info for mpg from API Ninjas
def get_mpg_info():
    mpg = {}
    mpg['make'] = input("Enter your car make: ")
    mpg['model'] = input("Enter your car model: ")
    mpg['year'] = input("Enter your car year: ")
    return mpg

def retrieve_mpg_data(mpg):
    mpg_headers = {
        'X-Api-Key': NINJA_API_KEY
    }
    mpg_params = {
        'make': mpg['make'],
        'model': mpg['model'],
        'year': mpg['year']
    }
    response = requests.get(NINJA_URL, headers=mpg_headers, params=mpg_params)
    if response.status_code == 200:
        print('Data retrieved successfully')
        with open('mpg_data.json', 'w') as f:
            json.dump(response.json(), f)
        print(response.json())
    else:
        print('Error retrieving data')
        print(response.status_code)
        print(response.text)
        os.exit(1)

# TEST
get_fuel_us()

mpg = get_mpg_info()
retrieve_mpg_data(mpg)
