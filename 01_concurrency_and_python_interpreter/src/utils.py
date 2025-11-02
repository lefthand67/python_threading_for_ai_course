import time


def print_numbers(n):
    """Print numbers."""
    for i in range(n):
        print(f"Number: {i}")
        time.sleep(1)


def print_letters(string):
    """Print letters."""
    for letter in string:
        print(f"Letter: {letter}")
        time.sleep(1)


def worker_loop(n):
    """Run worker thread."""
    for i in range(n):
        print("Worker:", i)
        time.sleep(0.5)
