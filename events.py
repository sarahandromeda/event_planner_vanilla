import csv
import shutil
from tempfile import NamedTemporaryFile
import settings
from inputs import NewEvent, QueryInput
from messages import Say

def write_file(data_dict=None):
    """
    Takes a list of dict objects representing each row of the CSV
    file, returned by Querying, Creating and New Event, and deleting
    an event functions. Writes new data to tempfile and replaces
    original CSV file with newly written tempfile. 
    """
    with NamedTemporaryFile('w+b', newline='', delete=False) as temp_file:
        writer = csv.DictWriter(temp_file, fieldnames = settings.FIELDS)
        writer.writeheader()
        if data_dict is not None:
            for row in data_dict:
                writer.writerow(row)
    shutil.move(temp_file.name, settings.FILE_NAME)

def read_file():
    """
    Reads CSV file into a dictionary.
    Returns list of dict objects. 
    """
    data = []
    with open(settings.FILE_NAME, 'a', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def add_event():
    """
    Opens current csv for reading current data and opens a temp file
    for writing. Reads current data into a list of dict objects. Then 
    appends new event data to the list and writes the data to the
    temp file. Moves temp file to current file location to overwrite
    file with new data. 
    Returns string representation of new event. 
    """
    new_event_data = list(NewEvent.new_event())
    with open(settings.FILE_NAME, 'a', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_event_data.append(row)
    write_file(new_event_data)
        

def remove_event():
    pass

def see_all():
    data = read_file()
    Say.event_string(data)

def see_upcoming(): 
    pass

def see_past():
    pass

def check_upcoming():
    pass

def reset_planner():
    """
    Rewrites CSV with only the header line. Overwrites all previous data
    inside the file. 
    """
    confirm = input('This is irreversible, are you sure you want to continue? y/n')
    if confirm.lower == 'n':
        return
    else:
        write_file()
    