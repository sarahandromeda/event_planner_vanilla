import time
from tracemalloc import start
import settings
import art

class Say:
    """
    Class methods that print relevant messages to the console.
    """

# General Display Messages

    @classmethod
    def hello(cls):
        print(art.header)
        time.sleep(1)
        print("""
------------------------------
Welcome to your Event Manager

To create a new event, simply enter the number '1' to begin.
You will be prompted for details about the event to create.
After you have at least 1 event, you can use the other menu
options to show upcoming or past events, delete events search 
events by location, time, and more!
-------------------------------
        """, end='')
        time.sleep(1)

    @classmethod
    def goodbye(cls):
        print("See you next time!")
        print('Closing planner', end='')
        for i in range(5):
            print('.', end='', flush=True)
            time.sleep(0.3)
        print('')

    @classmethod
    def proceed(cls):
        print('\nPress enter to continue.\n')

    @classmethod
    def show_menu(cls):
        print("""
Please select from the following options. 
Enter a single number corresponsing to the choice.

    1) Create an Event
    2) Show All Events
    3) Show Upcoming Events
    4) Show Past Events
    5) Search Events
    6) Delete Events
    7) Reset Planner**
    8) Exit

** This menu option is irreversible and will delete all of
your data. Use with caution.
        """)

    @classmethod
    def search_options(cls):
        print(
            '\nPlease enter numbers corresponding to the fields you\n' +
            'would like to search. You may enter more than one\n' +
            'number to narrow your search results.\n'
            )
        print("""
            1) Search by Organizer      4) Search by Date
            2) Search by Location       5) Search by Time
            3) Search by Type
            """)
        print(
            '\nEx. "2 4" will search by Location and Date\n' +
            '"1 2 4" will search by Organizer, Location and Date\n'
            )
    
    @classmethod
    def event_string(cls, data_dict):
        """
        Takes a list of event dict objects, loops through them, and
        prints a human readable string of each event.
        """
        for event in data_dict:
            organizer = event['organizer']
            event_name = event['event_name']
            event_type = event['event_type']
            start_time = event['start_datetime']
            formatted_time = start_time.strftime("%A, %B %-d, %Y at %-I:%M %p")
            location = event['location']
            print(
                f"\n{organizer} is hosting {event_name}, " +
                f"a {event_type}, on\n" +
                f"{formatted_time} " +
                f"in {location}!\n"
            )

# Input Prompt Messages

    @classmethod
    def askfor_event_name(cls):
        print('\nPlease enter name of event.\n')

    @classmethod
    def askfor_event_type(cls):
        print(
            '\nPlease enter the type of event.\n' +
            'Ex: Party, Reunion, Convention, etc.\n'
            )

    @classmethod
    def askfor_organizer(cls):
        print(
            '\nPlease enter the name of the event organizer.\n' + 
            'Include, at minimum, a first name.\n'
            )

    @classmethod
    def askfor_location(cls):
        print(
            '\nPlease enter the location of the event.\n' +
            'Include, at minimum, the state.\n'
            )

    @classmethod
    def askfor_date(cls):
        print(
            '\nPlease enter the date of the event.\n' +
            'Use MM/DD/YY format.\n'
            )

    @classmethod
    def askfor_time(cls):
        print(
            '\nPlease enter the time of the event.\n' +
            'Use HH:MM format also indicating AM or PM.\n' +
            'Ex. 04:30 PM\n'
            )

# Confirmation and Error messages

    @classmethod
    def confirm_deletion(cls, selection_dict):
        print("""
            
            Please review the selection(s):

            """)
        count = 0
        for event in selection_dict:
            print(
                f"{count}) {event['organizer']}'s " +
                f"{event['event_type']} " +
                f"on {event['start_datetime'].date()} " +
                f"at {event['start_datetime'].time()}\n\n"
            )
            count += 1
        print("""

            Enter the numbers of the events you would like to delete.
            Ex. "0 5 10" to delete events numbered respectively.
            To abort, type 'n' or just press enter.

            """)

    @classmethod
    def confirm_deleted(cls, object):
        print(f'\n{object} sucessfully deleted.\n')

    @classmethod
    def invalid_input(cls, response):
        print(f'\n{response} is invalid.\n')

    @classmethod
    def invalid_date(cls, response):
        print(
            f'\n{response} is invalid.\n' +
            'Please enter a date in format MM/DD/YY.\n'
            )

    @classmethod
    def invalid_time(cls, response):
        print(
            f'\n{response} is invalid.\n' +
            'Please enter time in HH:MM AM (or PM) format.\n'
            )