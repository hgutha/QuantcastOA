from .utils import build_cookie_map_from_logfile, find_most_active_cookies
import argparse


def main():
    parser = argparse.ArgumentParser(description="Find most active cookie(s) for a specified day.")
    parser.add_argument("file", help="Path to the cookie log file")
    parser.add_argument("-d", "--date", required=True, help="Date in YYYY-MM-DD format")
    args = parser.parse_args()

    cookie_map = build_cookie_map_from_logfile(args.file)
    most_active_cookies = find_most_active_cookies(cookie_map, args.date)

    for cookie in most_active_cookies:
        print(cookie)


if __name__ == '__main__':
    main()
