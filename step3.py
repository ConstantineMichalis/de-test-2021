from step1 import is_log_line
from step2 import get_dict
import re
from datetime import datetime

# You should not need to change this function
def log_parser(log_file):
    f = open(log_file)
    for line in f:
        if is_log_line(line):
            d = get_dict(line)
            d["message"] = clean_message(d["message"])
            d["timestamp"] = convert_to_iso(d["timestamp"])
            yield d

# [TODO]. Step 3a. 
# Clean the message value of your dict so that you remove
# the leading colons (`:`) and periods (`.`) before the message
def clean_message(message):
    pass


# [TODO]. Step 3b.
# Convert the timestamp value from its current format: DD/MM/YY HH:MM:SS
# to an ISO timestamp format: YYYY-MM-DD HH:MM:SS
def convert_to_iso(timestamp):
    pass


# YOU DON"T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == '__main__':
    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE
    expected_line2 = {
        "timestamp": "2021-11-03 08:51:01",
        "log_level": "INFO",
        "message": "locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf"
    }
    lp = log_parser("sample.log")
    _ = next(lp)
    actual = next(lp)

    if expected_line2 == actual:
        print("SUCCESS")
    else:
        print(
            "FAILURE: your second item from the generator was not as expected.\n"
            "Printing both expected and your output:\n")
        print(f"Expected: {expected_line2}")
        print(f"Generator Output: {actual}")
        
        if expected_line2.get("timestamp") == actual.get("timestamp"):
            print("The timestamp keys match")
        else:
            print("The timestamp keys do not match")

        if expected_line2.get("message") == actual.get("message"):
            print("The message keys match")
        else:
            print("The message keys do not match")
