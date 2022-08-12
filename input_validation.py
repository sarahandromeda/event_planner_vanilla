from datetime import datetime
import re
from messages import Say

# Input Verification Methods 
class InputVerification:
    def verify(self, response):
        """
        Requirement verification. Verifies that input response is not an empty
        string. 
        Function will ask user repeatedly for an input, if it is left blank,
        inside a loop eventually returning the response when valid. 
        """
        # Loop until response is not an empty string
        while not response:
            Say.invalid_input(response) 
            response = input()
        return response

    def verify_date(self, response):
        """
        Verifies that input response can be parsed into datetime object using 
        the requested date format: MM/DD/YY. 
        Function begins a loop and tries to parse datetime object from response.
        If it fails, prompt user again, continue the loop and try the next response.
        Returns first instance of valid response. 
        """
        response = self.verify(response)
        while True:
            try:
                datetime.strptime(response, "%m/%d/%y")
                break
            except ValueError:
                Say.invalid_date(response)
                response = input()
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
        response = self.verify(response)
        while True:
            try:
                datetime.strptime(response, "%I:%M %p")
                break
            except ValueError:
                Say.invalid_time(response)
                response = input()
                continue
        return response

    def verify_menu_selection(self, response):
        response = self.verify(response)
        while True:
            if re.search(r'\A[1-8]\Z', response):
                break
            else:
                Say.invalid_input(response)
                response = input()
                continue
        return response