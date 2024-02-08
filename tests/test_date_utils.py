import unittest
from most_active_cookie.date_utils import date_to_string, is_valid_date_format


class TestDateUtilsFunctions(unittest.TestCase):
    def test_is_valid_date_format(self):
        timestamp = "2018-12-09T14:19:00+00:00"
        expected_timestamp_string = "20181209"
        timestamp_string = date_to_string(timestamp)
        self.assertEqual(expected_timestamp_string, timestamp_string)

        date = "2018-03-08"
        expected_date_string = "20180308"
        date_string = date_to_string(date)
        self.assertEqual(expected_date_string, date_string)

    def test_is_valid_date_format_with_wrong_date_formats(self):
        invalid_dates = ["03-08-2018", "03/08/2018", "3-8-2018", "3/8/2018"]  # Invalid formats
        for date in invalid_dates:
            with self.assertRaises(ValueError):
                date_to_string(date)

    def test_is_valid_date_format_with_valid_february_date_1(self):
        date = "2018-02-28"
        expected_date_string = "20180228"
        date_string = date_to_string(date)
        self.assertEqual(expected_date_string, date_string)

    def test_is_valid_date_format_with_invalid_february_date(self):
        date = "2018-02-29"
        with self.assertRaises(ValueError):
            date_string = date_to_string(date)

    def test_is_valid_date_format_with_valid_february_date_leap_year(self):
        timestamp = "2020-02-29"
        expected_date_string = "20200229"
        date_string = date_to_string(timestamp)
        self.assertEqual(expected_date_string, date_string)

    def test_is_valid_date_format_with_invalid_february_leap_year(self):
        date = "2020-02-30"
        with self.assertRaises(ValueError):
            date_string = date_to_string(date)

    def test_date_to_string(self):
        timestamp = "2018-12-09T14:19:00+00:00"
        expected_timestamp_string = "20181209"
        timestamp_string = date_to_string(timestamp)
        self.assertEqual(expected_timestamp_string, timestamp_string)

        date = "2018-03-08"
        expected_date_string = "20180308"
        date_string = date_to_string(date)
        self.assertEqual(expected_date_string, date_string)


if __name__ == "__main__":
    unittest.main()