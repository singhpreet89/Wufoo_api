import csv

from helpers.Request_helper import Request
from config.config import configuration

class Parse_CSV:
    
    def __init__(self):
        self.__request_obj = Request()
        
        self.__file_name = configuration['file_name']
        
    def __parse(self):
        with open(self.__file_name) as csv_file:
            csv_dictionary = csv.DictReader(csv_file, delimiter=',')
            
            for row in csv_dictionary:
                print(row)
                self.__request_obj.get_post_entry(row)
            
    def get_csv_dictionary(self):
       self.__parse()
