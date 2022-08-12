import unittest
from unittest import mock 
from unittest import TestCase
import datetime
import inputs
from inputs import NewEvent
from input_validation import InputVerification
import query

class TestNewEvent(TestCase):
    @mock.patch('inputs.input', create=True)
    def test_new_event(self, mocked_input):
        mocked_input.side_effect = [
            'Birthday Bash', 
            'Birthday Party',
            'Jennifer Green',
            'Colorado',
            '08/22/22',
            '04:30 PM'
            ]
        result = NewEvent.new_event()
        expected = [{
            'event_name' : 'Birthday Bash',
            'event_type' : 'Birthday Party',
            'organizer' : 'Jennifer Green',
            'location' : 'Colorado',
            'start_datetime' : datetime.datetime(2022,8,22,16,30)
        }]
        self.assertEqual(result, expected)

class TestQueryEvent(TestCase):

    @mock.patch('query.input', create=True)
    def test_init(self, mocked_input):
        data_dict = [
            {
                'event_name' : 'Birthday',
                'event_type' : 'Party',
                'organizer' : 'Jennifer',
                'location' : 'Colorado',
                'start_datetime' : datetime.datetime(2022,8,22,16,30)
            },
            {
                'event_name' : 'How Have You Been',
                'event_type' : 'Reunion',
                'organizer' : 'Jennifer',
                'location' : 'Denver, Colorado',
                'start_datetime' : datetime.datetime(2023,5,22,17,30)
            },
            {
                'event_name' : 'The Meetup',
                'event_type' : 'Conference',
                'organizer' : 'William',
                'location' : 'Washington',
                'start_datetime' : datetime.datetime(2022,5,22,7,30)
            }
        ]

        mocked_input.side_effect = ['1']
        
        results = query.QueryEvent(event_list = data_dict)
        self.assertEqual(results.event_list, data_dict)
        self.assertEqual(results.matching_events, data_dict)


class TestInputVerification(TestCase):
    
    @mock.patch('input_validation.input', create=True)
    def test_verification(self, mocked_input):
        mocked_input.side_effect = ['', '', 'Hello']
        results = InputVerification().verify('')
        self.assertEqual(results, 'Hello')

    @mock.patch('validate.input', create=True)
    def test_date_verification(self, mocked_input):
        mocked_input.side_effect = ['03/15/22']
        results = InputVerification().verify_date('17/86/43')
        self.assertEqual(results, '03/15/22')

    @mock.patch('validate.input', create=True)
    def test_time_verification(self, mocked_input):
        mocked_input.side_effect = ['03:30 AM']
        results = InputVerification().verify_time('4567')
        self.assertEqual(results, '03:30 AM')





if __name__ == '__main__':
    unittest.main()
