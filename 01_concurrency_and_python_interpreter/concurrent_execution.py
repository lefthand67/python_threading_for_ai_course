import threading
import time

import utils


def main():
    """Run code."""
    start = time.perf_counter()

    t1 = threading.Thread(target=utils.print_numbers, args=(5,))
    t2 = threading.Thread(target=utils.print_letters, args=("abcde",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.perf_counter()

    print(f"Time: {round(end - start, 2)}")


if __name__ == "__main__":
    main()
