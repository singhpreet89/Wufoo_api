import json
import re

class Response:
        
    def __handle_response(self, result, counter):
        response_result = None
        
        if re.search('^[2][0-9][0-9]$', str(result.status_code)):
            response_result = self.__handle_success(result, counter)
                
        elif re.search('^[4][0-9][0-9]$', str(result.status_code)):
            response_result =  self.__handle_client_errors(result)
            
        elif re.search('^[5][0-9][0-9]$', str(result.status_code)):
            response_result = self.__handle_server_errors(result)
            
        return response_result
    
############################### SUCCESS ###############################      
    def __handle_success(self, result, counter):
        success_message = None
        
        if result.status_code == 200:
            # text = json.dumps(result.json(), indent = 4, sort_keys = True)
            # print(text) 
            # print("Length of List: " + str(len(result.json()['FieldErrors'])))
        
            validation_errors = ""
            for i in range(len(result.json()['FieldErrors'])):
                validation_errors = f"{validation_errors + result.json()['FieldErrors'][i]['ID']} --> {result.json()['FieldErrors'][i]['ErrorText']}\n" 
            success_message = f"\nVALIDATION ERROR in Row: {counter}\n{validation_errors}"
        
        elif result.status_code == 201:
            success_message =  f"\nEntry added for Row: {counter}\nLink: {result.json()['EntryLink']}"
        
        else:
            success_message =  f"Success code: {result.status_code}" 
        return success_message
    
############################### ERRORS ###############################      
    def __handle_client_errors(self, result):
        client_error_message = None
        
        if result.status_code == 421:
            client_error_message = f"Error code: {result.status_code}, You have exceeded your daily API usage."
        
        else:
            client_error_message = f"Error code: {result.status_code}"
        return client_error_message
            
    def __handle_server_errors(self, result):
         server_error_message = "Error code: {result.status_code},\nSend our support team the request you used, and we can take a closer look."
         return server_error_message
         
    def get_response(self, result, counter):
        return self.__handle_response(result, counter)