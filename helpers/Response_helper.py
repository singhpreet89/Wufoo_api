import json
import re

class Response:
        
    def __handle_response(self, result):
        if re.search('^[2][0-9][0-9]$', str(result.status_code)):
           self.__handle_success(result)
                
        elif re.search('^[4][0-9][0-9]$', str(result.status_code)):
           self.__handle_client_errors(result)
            
        elif re.search('^[5][0-9][0-9]$', str(result.status_code)):
           self.__handle_server_errors(result)
     
############################### SUCCESS ###############################      
    def __handle_success(self, result):
        if result.status_code == 200:
            # text = json.dumps(result.json(), indent = 4, sort_keys = True)
            # print(text) 
            # print("Length of List: " + str(len(result.json()['FieldErrors'])))
            
            print("\n----------")
            print("VALIDATION ERRORS: ")
            for i in range(len(result.json()['FieldErrors'])):
                    print(result.json()['FieldErrors'][i]['ID'] + " --> " + result.json()['FieldErrors'][i]['ErrorText'])
            print("----------\n")   
        
        elif result.status_code == 201:
            # text = json.dumps(result.json(), indent = 4, sort_keys = True)
            print("Entry added.\nLink: " + result.json()['EntryLink'] + "\n")
        
        else:
            print("Error code:", result.status_code) 
    
############################### ERRORS ###############################      
    def __handle_client_errors(self, result):
        if result.status_code == 421:
            print("Error code:", result.status_code , "You have exceeded your daily API usage.")
        else:
            print("Error code:", result.status_code)
            
    def __handle_server_errors(self, result):
         print("Error code:", result.status_code , "\n Send our support team the request you used, and we can take a closer look")
             
    def get_response(self, result):
        self.__handle_response(result)