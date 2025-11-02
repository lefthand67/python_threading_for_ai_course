import time

import utils


def main():
    """Run code."""
    start = time.perf_counter()

    utils.print_numbers(5)
    utils.print_letters("abcde")

    end = time.perf_counter()

    print(f"Time: {round(end - start, 2)}")


if __name__ == "__main__":
    main()
