import unittest
from unittest import mock 
from unittest import TestCase
import datetime
import inputs

class TestInputs(TestCase):
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
        result = inputs.new_event()
        expected = [{
            'event_name' : 'Birthday Bash',
            'event_type' : 'Birthday Party',
            'organizer' : 'Jennifer Green',
            'location' : 'Colorado',
            'start_datetime' : datetime.datetime(2022,8,22,16,30)
        }]
        self.assertEqual(result, expected)

class TestInputVerification(TestCase):
    
    @mock.patch('inputs.input', create=True)
    def test_verification(self, mocked_input):
        mocked_input.side_effect = ['', '', 'Hello']
        results = inputs.verify('')
        self.assertEqual(results, 'Hello')

    @mock.patch('inputs.input', create=True)
    def test_date_verification(self, mocked_input):
        mocked_input.side_effect = ['03/15/22']
        results = inputs.verify_date('17/86/43')
        self.assertEqual(results, '03/15/22')

    @mock.patch('inputs.input', create=True)
    def test_time_verification(self, mocked_input):
        mocked_input.side_effect = ['03:30 AM']
        results = inputs.verify_time('4567')
        self.assertEqual(results, '03:30 AM')


if __name__ == '__main__':
    unittest.main()
