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

def log_function_call(func):
    """
    Write Your Code Here.
    """

# ตัวอย่างการใช้งาน
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def devide(a, b):
    return a/b

if __name__ == "__main__":
    add(1,1)
    devide(10/0)
