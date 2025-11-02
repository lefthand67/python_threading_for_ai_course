import threading
import time

import utils


def main():
    """Run code."""
    print("Main: Starting threads...")

    start = time.perf_counter()

    t1 = threading.Thread(target=utils.print_numbers, args=(5,))
    t2 = threading.Thread(target=utils.print_letters, args=("abcde",))

    t1.start()
    t2.start()

    print("Main: Threads started. Waiting for them to finish...")

    t1.join()
    t2.join()

    end = time.perf_counter()

    print("Main: Both threads have finished.")
    print(f"Time: {round(end - start, 2)}")


if __name__ == "__main__":
    main()
