import unittest
from unittest.mock import patch, MagicMock
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_ymd_date(self, mock_urlopen):
        mocked_data = MagicMock()
        mocked_data.read.return_value = '{"currentDateTime": "2019-03-01"}'
        mocked_data.__enter__.return_value = mocked_data
        mock_urlopen.return_value = mocked_data
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen')
    def test_dmy_date(self, mock_urlopen):
        mocked_data = MagicMock()
        mocked_data.read.return_value = '{"currentDateTime": "01.03.2019"}'
        mocked_data.__enter__.return_value = mocked_data
        mock_urlopen.return_value = mocked_data
        self.assertEqual(what_is_year_now(), 2019)

    @patch('urllib.request.urlopen')
    def test_invalid_date(self, mock_urlopen):
        mocked_data = MagicMock()
        mocked_data.read.return_value = '{"currentDateTime": "Invalid date"}'
        mocked_data.__enter__.return_value = mocked_data
        mock_urlopen.return_value = mocked_data
        with self.assertRaises(ValueError):
            self.assertEqual(what_is_year_now(), 2019)


if __name__ == '__main__':
    unittest.main()
