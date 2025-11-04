import logging
import threading
import time


def main():
    """Run code."""
    logging.basicConfig(
        level=logging.DEBUG, format="%(relativeCreated)6d %(threadName)s %(message)s"
    )

    lock_a = threading.Lock()
    lock_b = threading.Lock()

    t1 = threading.Thread(target=thread, args=(lock_a, lock_b))
    t2 = threading.Thread(target=thread, args=(lock_b, lock_a))

    t1.start()
    t2.start()


def thread(lock_a, lock_b):
    """Start thread."""
    logging.debug("Started")
    with lock_a:
        logging.debug(f"Acquired lock {lock_a}")
        time.sleep(0.1)
        logging.debug(f"Trying to acquire lock {lock_b}...")
        # Try to acquire lock B, but only wait for 2 seconds.
        acquired = lock_b.acquire(timeout=2)
        if acquired:
            logging.debug(f"Acuired both {lock_a} and {lock_b}")
        else:
            logging.error(f"COULD NOT ACQUIRE LOCK {lock_b}! POTENTIAL DEADLOCK!")
        # Remember to release lock_b if the logic requires it.
    logging.debug("Thread exiting")


if __name__ == "__main__":
    main()
