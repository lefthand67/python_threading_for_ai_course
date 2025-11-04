import threading


def main():
    """Run code."""
    # Using an RLock
    r_lock = threading.RLock()

    def recursive_traverse(depth):
        print(f"Calling function: Depth {depth}")
        # Acquisition #1 (or #2, #3...) for this thread.
        with r_lock:
            if depth > 0:
                # Inner call acquires the same RLock successfully.
                recursive_traverse(depth - 1)
                # The RLock is only truly released after the outermost 'with' block exits.

    # This now works correctly and does not deadlock.
    recursive_traverse(2)


if __name__ == "__main__":
    main()
