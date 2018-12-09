import requests


class Employee():
    def __init__(self, first_name: str,last_name: str):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()

    def get_details(self, month):
        response = requests.get(f'http://comanyname.com/{self.last_name}/{self.first_name}/{month}')
        if response.ok:
            return response.text
        else:
            return 'API Failure'