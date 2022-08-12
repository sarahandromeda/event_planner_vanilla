import csv
import shutil
from datetime import datetime
from tempfile import NamedTemporaryFile
import settings

class File:
    """
    Describes the CSV file used and methods to access the file's
    data. 
    """    
    def write_file(data_dict=None):
        """
        May take a list of dict objects representing each row of the CSV
        file, returned by Querying, Creating and New Event, and deleting
        an event functions. Writes new data to tempfile and replaces
        original CSV file with newly written tempfile. 
        """
        FIELDS = [
            'event_name', 
            'event_type', 
            'organizer', 
            'location', 
            'start_datetime'
            ]

        with NamedTemporaryFile('w', newline='', delete=False) as temp_file:
            writer = csv.DictWriter(temp_file, fieldnames = FIELDS)
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
        with open(settings.FILE_NAME, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                row['start_datetime'] = datetime.strptime(
                    row['start_datetime'], 
                    "%Y-%m-%d %H:%M:%S"
                    )
                data.append(row)
        return data

