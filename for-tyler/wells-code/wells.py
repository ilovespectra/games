import textwrap

def generate_response(file_path, width):
    with open(file_path, "r") as f:
        response = f.read()
    wrapped_response = textwrap.fill(response, width=width)
    print("\033[47m\033[30m" + wrapped_response + "\033[0m")

generate_response("wells2.txt", 94)

