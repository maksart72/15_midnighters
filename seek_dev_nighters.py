import datetime
import json
import pytz
import requests


def load_attempts(pages):
    all_records = ()
    for page in range(pages):
        url = 'https://devman.org/api/challenges/solution_attempts/'
        details = {'page': page + 1}
        records_request = requests.get(url, params=details)
        records_json = json.loads(records_request.content)
        for records in records_json['records']:
            if records['timestamp'] is not None:
                timezone = pytz.timezone(records['timezone'])
                datetime_timezone = datetime.datetime.fromtimestamp(
                    records['timestamp'], timezone)
                if datetime_timezone.hour < 6:
                    all_records = all_records + (records['username'],)
    return set(all_records)


def print_midnighters(attempts_information):
    for developer in attempts_information:
        print(developer)


if __name__ == '__main__':
    pages_num = 10
    print_midnighters(load_attempts(pages_num))
