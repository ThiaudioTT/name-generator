import requests
import random

import endpoints

# Generates a random name based on get requests from the internet
def generateName():
    iChooseAPI = random.randint(0, endpoints.length - 1)
    response = requests.get(endpoints._list[iChooseAPI])

    if response.status_code == 200 and response.headers['content-type'] == 'application/json':
        return str(response.json()[0])
    else:
        print('Error: ' + str(response.status_code))
        return 'Error'


def main():
    print('Generating name...')
    print(generateName() + ' ' + generateName())

main()