import threading
import time


def main():
    """Run code."""
    print("Main: Start.")

    # Run worker thread
    worker_thread = threading.Thread(target=worker_loop, args=(5,))
    worker_thread.start()

    for i in range(5):
        print("Main: Check", i)
        if worker_thread.is_alive():
            print("Main: Worker thread is alive")
        time.sleep(0.5)

    worker_thread.join()

    print("Main: Done.")


def worker_loop(n):
    """Run worker thread."""
    for i in range(n):
        print("Worker:", i)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
