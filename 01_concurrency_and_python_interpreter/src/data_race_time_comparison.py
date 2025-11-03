import threading
import time

n = 100_000


def main():
    """Compare time."""
    result_bug = list()
    result_lock = list()

    m = 100
    for i in range(m):
        start = time.perf_counter()
        implement_bug()
        end = time.perf_counter()
        result_bug.append(end - start)

        start = time.perf_counter()
        implement_lock()
        end = time.perf_counter()
        result_lock.append(end - start)

    # mean time results
    mean_result_bug = sum(result_bug) / m
    mean_result_lock = sum(result_lock) / m

    # final difference
    times = mean_result_lock / mean_result_bug

    print("Mean time spent:")
    print(f"\tBug:\t{mean_result_bug:.4f}")
    print(f"\tLock:\t{mean_result_lock:.4f}")
    print(f"Lock is slower in {times:.2f} times.")
    print(f"Number of tests: {m}")


def implement_bug():
    """Run code."""
    counter = 0

    def increment_counter(n: int):
        """Increment the global global variable."""
        nonlocal counter
        for i in range(n):
            counter += 1

    thread1 = threading.Thread(target=increment_counter, args=(n,))
    thread2 = threading.Thread(target=increment_counter, args=(n,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


def implement_lock():
    """Run code."""
    counter = 0

    lock = threading.Lock()

    def increment_counter(n: int):
        """Increment the global global variable."""
        nonlocal counter
        for i in range(n):
            with lock:
                counter += 1

    thread1 = threading.Thread(target=increment_counter, args=(n,))
    thread2 = threading.Thread(target=increment_counter, args=(n,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()
