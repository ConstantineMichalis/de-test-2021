# You should not need to change this function
from step1 import is_log_line
from step2 import get_dict
from step3 import clean_message, convert_to_iso

# [TODO]. This function (log_parser) is currently the same as
# step3, except, it has a second argument that allows the user
# to define what set of log levels they want returned. If left
# unspecified or the default of None is provided then return
# all log levels. Otherwise if a str of a single log level or
# a list of log levels is provided then only those log levels
# should be returned from the generator.
def log_parser(log_file, levels=None):
    f = open(log_file)
    for line in f:
        if is_log_line(line):
            d = get_dict(line)
            d["message"] = clean_message(d["message"])
            d["timestamp"] = convert_to_iso(d["timestamp"])
            yield d


# YOU DON"T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == '__main__':
    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE
    first_info = {
        "timestamp": "2021-11-03 08:51:01",
        "log_level": "INFO",
        "message": "main: *************** RSVP Agent started ***************"
    }

    first_trace = {
        "timestamp": "2021-11-03 08:51:06",
        "log_level": "TRACE",
        "message": "read_physical_netif: Home list entries returned = 7"
    }

    first_warning = {
        "timestamp": "2021-11-03 08:51:06",
        "log_level": "WARNING",
        "message": "mailslot_create: setsockopt(MCAST_ADD) failed - EDC8116I Address not available."
    }


    expected_len = 57
    actual_len = len(list(log_parser("sample.log")))
    if  actual_len == expected_len:
        print("Check 1: SUCCESS")
    else:
        print("Check 1: FAILURE")
        print(f"Expected full log of {expected_len} lines to be returned. But only got {actual_len} lines")

    print("")
    expected_len -= 8
    actual_len = len(list(log_parser("sample.log", levels=["INFO", "WARNING"])))
    if actual_len == expected_len:
        print("Check 2: SUCCESS")
    else:
        print("Check 2: FAILURE")
        print(f"Expected log of {expected_len} lines (for INFO and WARNING levels) to be returned. But only got {actual_len} lines")
    print("")

    for i, expected, level in [(3, first_info, "INFO"), (4, first_trace, "TRACE"), (5, first_warning, "WARNING")]:
        first_item = next(log_parser("sample.log", levels=level))
        # print(i, expected, level)
        if expected == first_item:
            print(f"Check {i}: SUCCESS")
        else:
            print(f"Check {i}: FAILURE")
            print(
                f"Your first item from the generator should have been the first {level} in the sample log. "
                "Printing both expected and your output:"
            )
            print(f"Expected: {expected}")
            print(f"Generator Output: {first_item}")
        print("")