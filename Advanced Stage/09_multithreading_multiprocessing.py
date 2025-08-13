# ======================================
# Topic: Multithreading & Multiprocessing in Python
# --------------------------------------
# Python can run tasks in two different ways:
# - Multithreading → Many threads share the same program memory, good for waiting tasks (I/O-bound)
# - Multiprocessing → Many processes, each with its own Python interpreter, good for heavy CPU work
#
# The big difference:
# - Multithreading is NOT true parallel execution in Python because of the GIL (Global Interpreter Lock)
# - Multiprocessing bypasses the GIL and runs tasks in parallel on different CPU cores

import threading       # Module for creating and managing threads
import multiprocessing # Module for creating and managing processes
import time            # Module for measuring execution time and simulating delays

# -------------------------------
# Example 1: Multithreading
# -------------------------------
# This function will be run by each thread.
# It simulates a task that waits for something to finish (like downloading a file).
def thread_task(name):
    print(f"[Thread {name}] Starting")  # Prints when the thread starts
    time.sleep(2)  # Simulates a task that takes 2 seconds (like a network request)
    print(f"[Thread {name}] Finished")  # Prints when the thread finishes

# -------------------------------
# Example 2: Multiprocessing
# -------------------------------
# This function will be run by each process.
# It simulates a heavy calculation that uses CPU time.
def process_task(number):
    print(f"[Process {number}] Starting")  # Prints when the process starts
    total = 0
    # A loop to simulate heavy CPU computation
    for i in range(1, 5_000_000):  # 5 million iterations!
        total += i
    print(f"[Process {number}] Finished with total = {total}")  # Prints result

# -------------------------------
# Main Program
# -------------------------------
if __name__ == "__main__":
    # We put code inside "if __name__ == '__main__'" to avoid issues
    # when using multiprocessing on Windows/macOS.

    # ---------- Multithreading Demo ----------
    print("\n=== MULTITHREADING DEMO ===")
    start_time = time.time()  # Record the start time

    threads = []  # List to store thread objects
    for i in range(3):  # Create 3 threads
        t = threading.Thread(target=thread_task, args=(i,))  # Create a thread
        threads.append(t)  # Add to our list
        t.start()  # Start the thread (runs in background)

    # Wait for all threads to finish before continuing
    for t in threads:
        t.join()

    print(f"Multithreading total time: {time.time() - start_time:.2f} seconds\n")

    # ---------- Multiprocessing Demo ----------
    print("=== MULTIPROCESSING DEMO ===")
    start_time = time.time()  # Record the start time

    processes = []  # List to store process objects
    for i in range(3):  # Create 3 processes
        p = multiprocessing.Process(target=process_task, args=(i,))  # Create a process
        processes.append(p)  # Add to our list
        p.start()  # Start the process (runs in parallel)

    # Wait for all processes to finish before continuing
    for p in processes:
        p.join()

    print(f"Multiprocessing total time: {time.time() - start_time:.2f} seconds")
