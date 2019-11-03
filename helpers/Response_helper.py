import json
import re

class Response:
        
    def __handle_response(self, result):
        response_result = None
        
        if re.search('^[2][0-9][0-9]$', str(result.status_code)):
        #    return self.__handle_success(result)
            response_result = self.__handle_success(result)
                
        elif re.search('^[4][0-9][0-9]$', str(result.status_code)):
        #    return self.__handle_client_errors(result)
            response_result =  self.__handle_client_errors(result)
            
        elif re.search('^[5][0-9][0-9]$', str(result.status_code)):
        #    return self.__handle_server_errors(result)
            response_result = self.__handle_server_errors(result)
            
        return response_result
    
############################### SUCCESS ###############################      
    def __handle_success(self, result):
        success_message = None
        
        if result.status_code == 200:
            # text = json.dumps(result.json(), indent = 4, sort_keys = True)
            # print(text) 
            # print("Length of List: " + str(len(result.json()['FieldErrors'])))
            
            # print("\n----------")
            # print("VALIDATION ERRORS: ")
            
            validation_errors = ""
            for i in range(len(result.json()['FieldErrors'])):
                # print(result.json()['FieldErrors'][i]['ID'] + " --> " + result.json()['FieldErrors'][i]['ErrorText'])
                validation_errors = f"{validation_errors + result.json()['FieldErrors'][i]['ID']} --> {result.json()['FieldErrors'][i]['ErrorText']}\n"
            # print("----------\n")   
            success_message = f"----------\nVALIDATION ERRORS: \n{validation_errors}----------"
        elif result.status_code == 201:
            # text = json.dumps(result.json(), indent = 4, sort_keys = True)
            success_message =  f"Entry added.\nLink: {result.json()['EntryLink']} \n"
        
        else:
            success_message =  f"Success code: {result.status_code}" 
        return success_message
    
############################### ERRORS ###############################      
    def __handle_client_errors(self, result):
        client_error_message = None
        
        if result.status_code == 421:
            # print("Error code:", result.status_code , "You have exceeded your daily API usage.")
            client_error_message = f"Error code: {result.status_code}, You have exceeded your daily API usage."
        else:
            # print("Error code:", result.status_code)
            client_error_message = f"Error code: {result.status_code}"
        return client_error_message
            
    def __handle_server_errors(self, result):
        #  print("Error code:", result.status_code , "\n Send our support team the request you used, and we can take a closer look")
         server_error_message = "Error code: {result.status_code},\nSend our support team the request you used, and we can take a closer look."
         return server_error_message
         
    def get_response(self, result):
        return self.__handle_response(result)