import time


def print_numbers(n):
    """Print numbers."""
    for i in range(n):
        time.sleep(1)
        print(f"Number: {i}")


def print_letters(string):
    """Print letters."""
    for letter in string:
        time.sleep(1)
        print(f"Letter: {letter}")
