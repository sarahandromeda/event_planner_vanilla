import settings

class Say:
    """
    Class methods that print relevant messages to the console.
    """

    # Add methods for each message to display to terminal
    # Eg. list of search options
    # eg. prompts related to specific fields
    # eg. introduction
    # eg. instructions

    @classmethod
    def askfor_event_name(cls):
        print('Please enter name of event.')

    @classmethod
    def askfor_event_type(cls):
        print(
            'Please enter the type of event.\n' +
            'Ex: Party, Reunion, Convention, etc.'
            )

    @classmethod
    def askfor_organizer(cls):
        print(
            'Please enter the name of the event organizer.\n' + 
            'Include, at minimum, a first name.'
            )

    @classmethod
    def askfor_location(cls):
        print(
            'Please enter the location of the event.\n' +
            'Include, at minimum, the state.'
            )

    @classmethod
    def askfor_date(cls):
        print(
            'Please enter the date of the event.\n' +
            'Use MM/DD/YY format.'
            )

    @classmethod
    def askfor_time(cls):
        print(
            'Please enter the time of the event.\n' +
            'Use HH:MM format also indicating AM or PM.\n' +
            'Ex. 04:30 PM'
            )

    @classmethod
    def search_options(cls):
        print(
            'Please enter numbers corresponding to the fields you\n' +
            'would like to search. You may enter more than one\n' +
            'number to narrow your search results.'
            )
        print("""
            1) Search by Organizer      4) Search by Date
            2) Search by Location       5) Search by Time
            3) Search by Type
            """)
        print(
            'Ex. 24 will search by Location and Date\n' +
            '1 will search by Organizer only'
            )
    
    @classmethod
    def event_string(data_dict):
        """
        Takes a list of event dict objects, loops through them, and
        prints a human readable string of each event.
        """
        for event in data_dict:
            print(
                f"{event['organizer']} is hosting {event['event_name']}," +
                f"a {event['event_type']}, on\n" +
                f"{event['start_datetime']:%A, %B %-d, %Y at %-I:%-M %p}"
            )