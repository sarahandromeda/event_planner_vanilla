from datetime import datetime
from inputs import NewEvent, DeleteEvent
from query import QueryEvent
from messages import Say
from file import File


class SortData:
    by_datetime = lambda event: event['start_datetime']

class Action:
    def add_event():
        """
        Opens current csv for reading current data and opens a temp file
        for writing. Reads current data into a list of dict objects. Then 
        appends new event data to the list and writes the data to the
        temp file. Moves temp file to current file location to overwrite
        file with new data. 
        Returns string representation of new event. 
        """
        event_data = File.read_file()
        new_event_data = NewEvent.new_event()
        event_data.append(new_event_data)
        File.write_file(event_data)

    def see_all():
        event_data = File.read_file()
        Say.event_string(event_data)

    def see_upcoming():
        event_data = File.read_file()
        upcoming_events = []
        for event in event_data:
            if event['start_datetime'] > datetime.now():        
                upcoming_events.append(event)
        Say.event_string(upcoming_events)

    def see_past():
        event_data = File.read_file()
        past_events = []
        for event in event_data:
            if event['start_datetime'] < datetime.now():        
                past_events.append(event)
        Say.event_string(past_events)

    def search_events():
        event_data = File.read_file()
        print(event_data)
        event_query = QueryEvent(event_data)
        results = event_query.query_events()
        Say.event_string(results)

    def remove_event():
        event_data = File.read_file()
        event_query = QueryEvent(event_data)
        results = event_query.query_events()
        DeleteEvent.confirm_delete(results)

    def reset_planner():
        """
        Rewrites CSV with only the header line. Overwrites all previous data
        inside the file. 
        """
        confirm = input('This is irreversible, are you sure you want to continue? y/n')
        if confirm.lower == 'n':
            return
        else:
            File.write_file()
        