from datetime import datetime
from inputs import QueryInput

class QueryEvent:
    """
    Creates a QueryEvent instance by passing the event_list
    and the query_dict is generated using the method within
    the QueryInput class. 
    """
    def __init__(self, event_list):
        self.event_list = event_list
        self.query = QueryInput().generate_query_dict()
        self.matching_events = []

    def query_events(self):
        """
        Searches query dict, representing queries by
        {<field to search>: <search param>}. For each field, call
        query function matching field, passing the search param 
        as the argument.
        Returns list of matching event dict objects.
        """

        for field, param in self.query.items():
            if field == '1':
                self._by_organizer(param)
            elif field == '2':
                self._by_location(param)
            elif field == '3':
                self._by_type(param)
            elif field == '4':
                self._by_date(param)
            elif field == '5':
                self._by_time(param)
        return self.matching_events

    # remove items from match_list while looping event_list to avoid issues
    def _by_organizer(self, param):
        """
        Takes a search parameter argument and updates self.event_list
        by removing objects that do not match search parameter.
        Returns nothing but updates self.event_list.
        """
        for event in self.event_list:
            # event is a dictionary representing the event
            organizer = event['organizer'].lower()
            print(param)
            print(organizer)
            if param.lower() not in organizer:
                for i in range(len(self.event_list)):
                    if self.matching_events[i] == event:
                        del self.matching_events[i]


    def _by_location(self, param):
        """
        Same functionality as by_organizer function.
        """
        for event in self.event_list:
            # event is a dictionary representing the event
            location = event['location'].lower()
            print(event)
            if param.lower() in location:
                self.matching_events.append(event)


    def _by_type(self, param):
        """
        Same functionality as by_organizer function.
        """
        for event in self.event_list:
            # event is a dictionary representing the event
            event_type = event['event_type'].lower()
            if param.lower() not in event_type:
                for i in range(len(self.event_list)-1):
                    if self.matching_events[i] == event:
                        del self.matching_events[i]

    def _by_date(self, param):
        """
        Same functionality as by_organizer function. This function
        searches only the date of the datetime object representing 
        the start_datetime field.
        """
        for event in self.event_list:
            # event is a dictionary representing the event
            start_datetime = event['start_datetime'] # a datetime object
            param_datetime = datetime.strptime(param, "%m/%d/%y")
            if not start_datetime.date() == param_datetime.date():
                for i in range(len(self.event_list)-1):
                    if self.matching_events[i] == event:
                        del self.matching_events[i]


    def _by_time(self, param):
        """
        Same functionality as by_organizer function. This function
        searches only the time of the datetime object representing 
        the start_datetime field.
        """
        for i in range(len(self.event_list) - 1):
            # event is a dictionary representing the event
            event = self.event_list[i]
            start_datetime = event['start_datetime'] # a datetime object
            param_datetime = datetime.strptime(param, "%I:%M %p")
            if not start_datetime.time() == param_datetime.time():
                for i in range(len(self.matching_events) - 1):
                    if self.matching_events[i] == event:
                        del self.matching_events[i]