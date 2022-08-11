from datetime import datetime

# Input Verification Methods 
class InputVerification:
    def verify(self,response):
        """
        Requirement verification. Verifies that input response is not an empty
        string. 
        Function will ask user repeatedly for an input, if it is left blank,
        inside a loop eventually returning the response when valid. 
        """
        # Loop until response is not an empty string
        while not response: 
            response = input('Please enter a valid response.\n')
        return response

    def verify_date(self,response):
        """
        Verifies that input response can be parsed into datetime object using 
        the requested date format: MM/DD/YY. 
        Function begins a loop and tries to parse datetime object from response.
        If it fails, prompt user again, continue the loop and try the next response.
        Returns first instance of valid response. 
        """
        while True:
            try:
                datetime.strptime(response, "%m/%d/%y")
                break
            except ValueError:
                response = input('Please enter a date in format MM/DD/YY.')
                continue
        return response


    def verify_time(self,response):
        """
        Verifies that input response can be parsed into a datetime object using
        the requested time format: HH:MM AM or PM.
        Function begins a loop and tries to parse datetime object from response.
        If it fails, prompt user again, continue the loop and try the next response.
        Returns first instance of valid response.
        """
        while True:
            try:
                datetime.strptime(response, "%I:%M %p")
                break
            except ValueError:
                response = input('Please enter time in HH/MM AM (or PM) format using 12-hour clock.')
                continue
        return response