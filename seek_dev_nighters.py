import datetime
import json
import pytz
import requests


def load_attempts():
    pages = 10
    all_records = []
    for page in range(pages):
        url = 'https://devman.org/api/challenges/solution_attempts/'
        details = {'page': page + 1}
        records_request = requests.get(url, params=details)
        records_json = json.loads(records_request.content)
        for records in records_json['records']:
            records_info = [records['username'],
                            records['timestamp'], records['timezone']]
            all_records.append(records_info)
    return all_records


def get_midnighters(attempts_information):
    midnighters = []
    for attempt in attempts_information:
        if bool(attempt[1]):
            timezone = pytz.timezone(attempt[2])
            datetime_timezone = datetime.datetime.fromtimestamp(attempt[1], timezone)
            if datetime_timezone.hour < 6:
                midnighters.append(attempt[0])
    return set(midnighters)

if __name__ == '__main__':
    midnighters_set = get_midnighters(load_attempts())
    for midnight_user in midnighters_set:
        print(midnight_user)
