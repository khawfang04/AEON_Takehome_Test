"""
log_decorator.py

This file contains a decorator for logging function calls.
Candidates are expected to implement a decorator that:

- Logs the name of the function being called
- Records the date and time of execution
- Displays the input arguments and keyword arguments
- Works with any function, regardless of its signature
- Handles and logs any exceptions that occur during execution

This task is designed to assess the candidate's understanding of decorators
and their ability to write reusable and maintainable code.
"""


import functools
import datetime
import time

def log_function_call(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ts = datetime.datetime.now().isoformat(sep=' ', timespec='seconds')
        func_name = func.__name__
        print(f"[{ts}] Calling {func_name} with args={args} kwargs={kwargs}")
        start = time.time()
        try:
            result = func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"[{ts}] {func_name} returned {result!r} (elapsed {elapsed:.4f}s)")
            return result
        except Exception as e:
            elapsed = time.time() - start
            print(f"[{ts}] Exception in {func_name} after {elapsed:.4f}s: {e!r}")
            raise

    return wrapper

# ตัวอย่างการใช้งาน
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def devide(a, b):
    return a/b

if __name__ == "__main__":
    
    try:
        add(1,1)
        devide(10,0)
    except Exception as e:
        print(f"Caught exception in main: {e}")
