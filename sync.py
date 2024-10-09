import requests
import datetime

def get_people(pers_id):
    return requests.get(f'https://swapi.py4e.com/api/people/{pers_id}/').json()

def main():
    response_01 = get_people(1)
    response_02 = get_people(2)
    response_03 = get_people(3)
    response_04 = get_people(4)

    print(response_01, response_02, response_03, response_04)

start = datetime.datetime.now()
main()
print(datetime.datetime.now() - start)