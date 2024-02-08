import unittest
from most_active_cookie.utils import build_cookie_map_from_logfile, find_most_active_cookies


class TestUtilsFunctions(unittest.TestCase):
    def setUp(self):
        self.expected_cookie_map_1 = {
            "20181209": {"AtY0laUfhglK3lC7": 2, "SAZuXPGUrfbcn5UA": 1, "5UAVanZf6UtGyKVS": 1},
            "20181208": {"SAZuXPGUrfbcn5UA": 1, "4sMM2LxV07bPJzwf": 1, "fbcn5UAVanZf6UtG": 1},
            "20181207": {"4sMM2LxV07bPJzwf": 1}
        }
        self.expected_cookie_map_2 = {
            "20181209": {"cookie1": 2, "cookie2": 1},
            "20181208": {"cookie1": 1, "cookie3": 1}
        }

    def test_build_cookie_map_from_logfile_missing_logfile(self):
        with self.assertRaises(FileNotFoundError):
            cookie_map = build_cookie_map_from_logfile("")

    def test_build_cookie_map_from_logfile(self):
        cookie_map = build_cookie_map_from_logfile("cookie_log.csv")
        self.assertEqual(self.expected_cookie_map_1, cookie_map)

    def test_find_most_active_cookies_with_non_existing_date(self):
        specified_date = "2023-02-07"
        expected_most_active_cookies = []
        most_active_cookies = find_most_active_cookies(self.expected_cookie_map_1, specified_date)
        self.assertEqual(most_active_cookies, expected_most_active_cookies)

    def test_find_most_active_cookies(self):
        specified_date = "2018-12-08"
        expected_most_active_cookies = ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]
        most_active_cookies = find_most_active_cookies(self.expected_cookie_map_1, specified_date)
        self.assertEqual(most_active_cookies, expected_most_active_cookies)

        specified_date = "2018-12-09"
        expected_most_active_cookies = ["cookie1"]
        most_active_cookies = find_most_active_cookies(self.expected_cookie_map_2, specified_date)
        self.assertEqual(most_active_cookies, expected_most_active_cookies)

        specified_date = "2018-12-07"
        most_active_cookies = find_most_active_cookies(self.expected_cookie_map_2, specified_date)
        self.assertEqual(most_active_cookies, [])


if __name__ == "__main__":
    unittest.main()
