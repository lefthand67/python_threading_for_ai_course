import threading


def main():
    """Run code."""
    counter = 0
    n = 100_000

    def increment_counter(n: int):
        """Increment the global global variable."""
        nonlocal counter
        for i in range(n):
            counter += 1

    print("Counter:", counter)

    thread1 = threading.Thread(target=increment_counter, args=(n,))
    thread2 = threading.Thread(target=increment_counter, args=(n,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Counter:", counter)


if __name__ == "__main__":
    main()
