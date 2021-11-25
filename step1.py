# This is a basic generator that will return
# 1 line of the log file at a time
# You should not need to change this function
def log_parser(log_file):
        f = open(log_file)
        for line in f:
            if is_log_line(line):
                yield line

# [TODO]. Update the is_log_line function below to skip lines that
# are not log lines that have a timestamp, error type and message.
# e.g. lines 1, 3, 7 and 37 are all examples of lines (from sample.log)
# that would be filtered out. There will be no perfect way to do this just
# decide what you think is reasonable to get the test to pass.
# The only thing you are not allowed to do is filter out log lines based on the
# exact row numbers you want to remove.
def is_log_line(line):
    return True


# YOU DON"T NEED TO CHANGE ANYTHING BELOW THIS LINE
if __name__ == "__main__":
    # ---- OUTPUT --- #
    # You can print out each line of the log file line by line
    # by uncommenting this code below
    # for i, line in enumerate(log_parser("sample.log")):
    #     print(i, line)

    # ---- TESTS ---- #
    # DO NOT CHANGE
    with open("tests/step1.log") as f:
        test_lines = f.readlines()
    actual_out = list(log_parser("sample.log"))

    if actual_out == test_lines:
        print("SUCCESS")
    else:
        print(
            "FAILURE: your log_parser produced unexpecting lines.\n"
            "Writing to failure.log if you want to compare it to tests/step1.log"
        )
        with open("failured-output.log", "w") as f:
            f.writelines(actual_out)
