from helpers.Parse_helper import Parse_CSV
from helpers.Request_helper import Request
from helpers.Response_helper import Response

class Request_controller:
        
    def __init__(self):
        self.parsed_rows = None
        self.result = None
        
    def get_parsed_file(self):
        parse = Parse_CSV()
        rows = parse.get_parsed_rows()
        self.parsed_rows = rows
        
    def send_request(self):
        # print(self.parsed_rows)
        request = Request()
        
        count = 0
        for row in self.parsed_rows:
            # print(row)
            self.result = request.post_entry(row)
            self.handle_response(count + 1)
            count += 1
    
    def handle_response(self, counter):
        response = Response()
        res = response.get_response(self.result, counter)
        print(res)
        
    def start(self):
        self.get_parsed_file()
        self.send_request()

obj = Request_controller()
obj.start()