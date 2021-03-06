import requests

from config.config import configuration

class Request:
    def __init__(self):
        self.__base_url = configuration['BASE_URL']
        self.__username = configuration['USERNAME']
        self.__password = configuration['PASSWORD']
        self.__form_hash = configuration['FORM_HASH']
        self.__auth_values = (self.__username, self.__password)
        
    def post(self, row):
        
        # Getting the field id's to be sent in the payload
        # response = requests.get(self.__base_url + '/forms/' + self.__form_hash +'/fields.json', params={'q':'system=true'}, auth = self.__auth_values)
        # print(json.dumps(response.json(), indent = 4, sort_keys = True))
        # print("\n----------\n") 
        
        result = requests.post(self.__base_url + '/forms/' + self.__form_hash +'/entries.json', data = row, auth = self.__auth_values)
        # print(result.status_code) 
        return result