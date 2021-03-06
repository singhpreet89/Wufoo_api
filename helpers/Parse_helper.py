import csv

from config.config import configuration

class Parse_CSV:
         
    def __init__(self):
        self.__file_name = configuration['FILE_NAME']
        
    def get_parsed_rows(self):
        with open(self.__file_name) as csv_file:
            csv_dictionary = csv.DictReader(csv_file, delimiter=',')
            parsed_rows_list =[]
            for row in csv_dictionary:
                # print(row)
                parsed_rows_list = parsed_rows_list + [row]
        return parsed_rows_list 