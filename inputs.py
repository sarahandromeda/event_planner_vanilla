from datetime import datetime
from input_validation import InputVerification as validate
from messages import Say

# Input Request Methods
class Menu:
    def get_selection():
        """
        Prompts user for an input related to menu options.
        Acccepts user input of number 1-8.
        Return selection as a string. 
        """
        response = validate().verify_menu_selection(input())
        return response

class NewEvent:
    """
    Class housing function to request input from user to create
    a new event.
    Returns new_event dict representing the fields as keys and
    inputs as the values.
    """
    def new_event():
        """
        Requests input from users relevant to a new event for each 
        field represented in the CSV file. Uses validation methods
        from input_validation module to verify correct inputs. 
        Returns a dictionary object with the keys representing the
        fields and the values representing the user's data. 
        """
        new_event = {}

        Say.askfor_event_name()
        new_event['event_name'] = validate().verify(input())

        Say.askfor_event_type()
        new_event['event_type'] = validate().verify(input())

        Say.askfor_organizer()
        new_event['organizer'] = validate().verify(input())

        Say.askfor_location()
        new_event['location'] = validate().verify(input())

        Say.askfor_date()
        start_date = validate().verify_date(input())

        Say.askfor_time()
        start_time = validate().verify_time(input())

        time = start_date + ' ' + start_time
        new_event['start_datetime'] = datetime.strptime(time, "%m/%d/%y %I:%M %p")
        return new_event

class QueryInput:
    """
    Class housing methods to request search query from user.
    Use QueryInput.generate_query_dict to preform necessary
    functions to return query dict.
    """

    def _get_query_list(self):
        """
        Displays a list of search choices and asks user to indicate 
        which search functions they would like to use. Accepts input
        as string of numbers representing each search query. 
        ex: '123'
        Sets query_list var to list of each number from input. 
        ex: ['1', '2', '3']
        """
        
        Say.search_options()
        response = validate().verify(input())
        self.query_list = [i for i in response if not i == ' ']

    def _get_query_params(self):
        """
        Requests input from user with message prompting user for
        specific parameters for each search they'd like to preform.
        Sets query_params var to list of responses.
        """

        self.query_params = []
        for option in self.query_list:
            if option == '1':
                Say.askfor_organizer()
                response = validate().verify(input())
                self.query_params.append(response)
            elif option == '2':
                Say.askfor_location()
                response = validate().verify(input())
                self.query_params.append(response)
            elif option == '3':
                Say.askfor_event_type()
                response = validate().verify(input())
                self.query_params.append(response)
            elif option == '4':
                Say.askfor_date()
                response = validate().verify_date(input())
                self.query_params.append(response)
            elif option == '5':
                Say.askfor_time()
                response = validate().verify_time(input())
                self.query_params.append(response)

    def generate_query_dict(self):
        """
        Calls class methods to set query_list and query_params.
        Generates and returns a dictionary made from the 2 lists.
        """

        self._get_query_list()
        self._get_query_params()
        query_dict = dict(zip(self.query_list, self.query_params))

        return query_dict

class DeleteEvent:
    def confirm_delete(data_dict):
        Say.confirm_deletion(data_dict)
        response = input()
        if not response or response.lower() == 'n':
            confirmed = []
            return confirmed
        confirmed = []
        response = [i for i in response if not i == ' ']
        for number in response:
            try:
                del data_dict[number]
                Say.confirm_deleted(number)
            except IndexError:
                Say.invalid_input(number)
        
            