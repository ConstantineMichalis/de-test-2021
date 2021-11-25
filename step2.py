from step1 import is_log_line

# You should not need to change this function
def log_parser(log_file):
    f = open(log_file)
    for line in f:
        if is_log_line(line):
            yield get_dict(line)

# [TODO]. The generator should now return a dict that contains the
# keys "timestamp", "log_level", and "message".
# See the expected variable used in the test below to see what we
# expected to get as the first item from the generator.
def get_dict(line):
    """
    Takes a log line and returns a dict with
    `timestamp`, `log_level`, `message` keys
    """
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
    expected = {
        "timestamp": "03/11/21 08:51:01",
        "log_level": "INFO",
        "message": ":.main: *************** RSVP Agent started ***************"
    }
    actual = next(log_parser("sample.log"))

    if expected == actual:
        print("SUCCESS")
    else:
        print(
            "FAILURE: your first item from the generator was not as expected.\n"
            "Printing both expected and your output:\n")
        print(f"Expected: {expected}")
        print(f"Generator Output: {actual}")
