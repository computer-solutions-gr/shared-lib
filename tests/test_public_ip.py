import unittest
from unittest.mock import patch

from requests import Timeout

from cssalib.misc import public_ip

class TestPublicIP(unittest.TestCase):

    @patch('requests.get') 
    def test_valid(self, mock_get):
        mock_get.return_value.json.return_value = {'ip': '1.2.3.4'}
        result = public_ip()
        self.assertEqual(result, '1.2.3.4')

    def test_request_failure(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = ConnectionError
            with self.assertRaises(ConnectionError):
                public_ip()

    def test_invalid_json(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {'not_ip': 'value'}
            with self.assertRaises(KeyError):
                public_ip()

    def test_timeout(self):
        with patch('requests.get') as mock_get:
            mock_get.side_effect = Timeout
            with self.assertRaises(Timeout):
                public_ip()