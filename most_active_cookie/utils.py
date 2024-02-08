from .date_utils import date_to_string


def build_cookie_map_from_logfile(file_path):
    cookie_map = {}
    with open(file_path, 'r') as f:
        for line in f.readlines()[1:]:
            # Split each line of the log file into a cookie and its corresponding timestamp
            cookie, log_timestamp = line.split(',')
            cookie, log_timestamp = cookie.strip(), log_timestamp.strip()
            # Convert timestamp into uniform string format "YYYYMMDD"
            log_timestamp_string = date_to_string(log_timestamp)
            # Check if cookie_map has timestamp, if not then initialize empty map for that timestamp
            if log_timestamp_string not in cookie_map:
                cookie_map[log_timestamp_string] = {}
            # Add cookie for this timestamp and keep its frequency
            cookie_map[log_timestamp_string][cookie] = cookie_map[log_timestamp_string].get(cookie, 0) + 1
    #  cookie_map structure = {date: cookie: freq}
    return cookie_map


def find_most_active_cookies(cookie_map, specified_date):
    # Convert user inputted date into uniform string format "YYYYMMDD"
    specified_date_string = date_to_string(specified_date)
    if specified_date_string not in cookie_map:
        print("No cookies found on this date.")
        return []

    most_active_cookie_max_freq = 0
    for cookie in cookie_map[specified_date_string]:
        # Find this cookie's frequency on this date
        cookie_freq = cookie_map[specified_date_string][cookie]
        # Update most active cookie frequency
        most_active_cookie_max_freq = max(most_active_cookie_max_freq, cookie_freq)

    most_active_cookies = []
    # Find all cookies that are seen the most times on that date and append to a list
    for cookie in cookie_map[specified_date_string]:
        if cookie_map[specified_date_string][cookie] == most_active_cookie_max_freq:
            most_active_cookies.append(cookie)

    return most_active_cookies
