import textwrap
import time
import sys

def generate_response(file_path, width, typing_speed):
    with open(file_path, "r") as f:
        response = f.read()
    wrapped_response = textwrap.fill(response, width=width)
    for char in wrapped_response:
        print("\033[47m\033[30m" + char, end='')
        sys.stdout.flush()
        time.sleep(typing_speed)
    print("\033[0m")

generate_response("../txt/mommy_290px.txt", 290, 0.0002)
