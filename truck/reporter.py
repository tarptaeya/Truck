import sys

abort_on_error = True

def report_error(message):
    print(message)
    if abort_on_error: sys.exit(0)
