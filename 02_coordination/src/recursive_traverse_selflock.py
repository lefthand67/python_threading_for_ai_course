import threading


def main():
    """Run code."""
    # Using a standard Lock
    lock = threading.Lock()

    def recursive_traverse(depth):
        print(f"Calling function: Depth {depth}")
        with lock:  # First acquisition here...
            if depth > 0:
                # ...Problem: We try to acquire the same lock AGAIN here!
                recursive_traverse(depth - 1)

    # This will cause a deadlock.
    # The thread will block forever on the inner `with lock` call.
    recursive_traverse(2)


if __name__ == "__main__":
    main()
