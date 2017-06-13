import argparse
import textwrap
from datetime import datetime, time
from collections import Counter

import requests
from pytz import timezone


def load_attempts() -> dict:
    api_url = "https://devman.org/api/challenges/solution_attempts"
    current_page = 1
    pages = 1
    while current_page <= pages:
        response = requests.get(api_url, params={"page": current_page}).json()
        pages = response["number_of_pages"]
        current_page += 1
        for record in response["records"]:
            yield record


def is_after_midnignt(timestamp: str,
                      usr_timezone: str,
                      night_shift: int) -> bool:

    attempt_timestamp = timestamp
    if attempt_timestamp:
        attempt_time = datetime.fromtimestamp(
                            attempt_timestamp, timezone(usr_timezone)).time()

        return time(0) < attempt_time < time(night_shift)


def get_midnighters(night_shift: int) -> list:
    user_and_attempts = []
    for record in load_attempts():
        user_name = record["username"]
        attempt_time = is_after_midnignt(
                                         record["timestamp"],
                                         record["timezone"],
                                         night_shift)
        if attempt_time:
            user_and_attempts.append(user_name)
    midnighters = Counter(user_and_attempts).most_common()
    return midnighters


def parse_arg() -> argparse:
    parser = argparse.ArgumentParser(
                formatter_class=argparse.RawDescriptionHelpFormatter,
                description=textwrap.dedent('''\
                                    *** Night Owls Detector ***
            -------------------------------------------------------------------
            |   The script shows pupils of education project DEVMAN.org who   |
            |   send commits with solutions after midnight local time.        |
            -------------------------------------------------------------------
                                            '''
                                            )
                                )
    parser.add_argument("-n", "--nightshift",
                        type=int,
                        default=6,
                        help="Night shift length (by default 6 hrs, 12am-6am)"
                        )
    return parser.parse_args().nightshift


def console_output(midnighters: list) -> None:
    for midnighter in midnighters:
        print("Midnighter: {}. Amount attempts after midnight: {}".
              format(midnighter[0], midnighter[1]))


def main():
    night_shift = parse_arg()
    midnighters = get_midnighters(night_shift)
    console_output(midnighters)


if __name__ == '__main__':

    main()
