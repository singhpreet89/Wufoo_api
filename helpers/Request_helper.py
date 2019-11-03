import requests

from helpers.Response_helper import Response
from config.config import configuration

class Request:
    def __init__(self):
        self.__response_obj = Response()
         
        self.__base_url = configuration['base_url']
        self.__username = configuration['username']
        self.__password = configuration['password']
        self.__form_hash = configuration['form_hash']
        self.__auth_values = (self.__username, self.__password)
        
    def __post_entry(self, row):
        
        # Getting the field id's to be sent in the payload
        # response = requests.get(self.__base_url + '/forms/' + self.__form_hash +'/fields.json', params={'q':'system=true'}, auth = self.__auth_values)
        # print(json.dumps(response.json(), indent = 4, sort_keys = True))
        # print("\n----------\n") 
        
        result = requests.post(self.__base_url + '/forms/' + self.__form_hash +'/entries.json', data = row, auth = self.__auth_values)
        print(result.status_code) 
        
        self.__response_obj.get_response(result)
        
    def get_post_entry(self, row):
        self.__post_entry(row)