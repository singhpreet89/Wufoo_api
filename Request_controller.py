from helpers.Parse_helper import Parse_CSV

class Request_controller:
        
    def __init__(self):
        self.obj = Parse_CSV()
        
    def make_request(self):
        self.obj.get_csv_dictionary()
        

obj = Request_controller()
obj.make_request()