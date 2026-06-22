"""
Real-World Example: Multiprocessing for CPU-bound Tasks

Scenario: Factorial Calculation

Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance.
"""

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorials of a given number
def computer_factorial(number):
    print(f"Computing factorial of {number}")

    result = math.factorial(number)

    print(f"Factorial of {number} is {result}")

    return result


if __name__ == "__main__":

    numbers = [5000, 6000, 7000, 8000]

    start_time = time.time()

    # Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial, numbers)

    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")




#     ### Extracted Full Code

# ```python
# """
# Real-World Example: Multiprocessing for CPU-bound Tasks

# Scenario: Factorial Calculation

# Factorial calculations, especially for large numbers,
# involve significant computational work. Multiprocessing
# can be used to distribute the workload across multiple
# CPU cores, improving performance.
# """

# import multiprocessing
# import math
# import sys
# import time

# # Increase the maximum number of digits for integer conversion
# sys.set_int_max_str_digits(100000)

# # Function to compute factorials of a given number
# def computer_factorial(number):
#     print(f"Computing factorial of {number}")

#     result = math.factorial(number)

#     print(f"Factorial of {number} is {result}")

#     return result


# if __name__ == "__main__":

#     numbers = [5000, 6000, 7000, 8000]

#     start_time = time.time()

#     # Create a pool of worker processes
#     with multiprocessing.Pool() as pool:
#         results = pool.map(computer_factorial, numbers)

#     end_time = time.time()

#     print(f"Results: {results}")
#     print(f"Time taken: {end_time - start_time} seconds")
# ```

# ---

# # What is Factorial?

# Example:

# ```python
# 5!
# ```

# means:

# ```text
# 5 × 4 × 3 × 2 × 1
# = 120
# ```

# Example:

# ```python
# math.factorial(5)
# ```

# Output:

# ```text
# 120
# ```

# ---

# # Why Multiprocessing Here?

# The instructor is demonstrating a **CPU-Bound Task**.

# ### CPU-Bound

# Tasks where CPU does most of the work.

# Examples:

# ```text
# Factorial Calculation
# Machine Learning Training
# Image Processing
# Video Rendering
# Matrix Multiplication
# ```

# ---

# # Why Not Multithreading?

# Because Python has:

# ```text
# GIL
# (Global Interpreter Lock)
# ```

# For CPU-heavy tasks:

# ```text
# Threads can't fully utilize multiple CPU cores.
# ```

# So we use:

# ```python
# multiprocessing
# ```

# ---

# # Understanding the Code

# ## Imports

# ```python
# import multiprocessing
# import math
# import sys
# import time
# ```

# ### math

# Used for:

# ```python
# math.factorial()
# ```

# ### multiprocessing

# Creates multiple processes.

# ### time

# Measures execution time.

# ### sys

# Changes Python settings.

# ---

# ## This Strange Line

# ```python
# sys.set_int_max_str_digits(100000)
# ```

# ### Why?

# Factorial of 8000 is HUGE.

# ```python
# math.factorial(8000)
# ```

# contains thousands of digits.

# When Python tries:

# ```python
# print(result)
# ```

# it converts the number to a string.

# Python has a safety limit.

# This line increases that limit.

# ---

# # Function

# ```python
# def computer_factorial(number):
# ```

# Receives:

# ```python
# 5000
# 6000
# 7000
# 8000
# ```

# one at a time.

# ---

# ## Calculate

# ```python
# result = math.factorial(number)
# ```

# Example:

# ```python
# math.factorial(5)
# ```

# returns:

# ```text
# 120
# ```

# ---

# # Main Block

# ```python
# if __name__ == "__main__":
# ```

# Required for multiprocessing.

# Without it:

# ```text
# Windows may create infinite child processes.
# ```

# ---

# # Input

# ```python
# numbers = [5000,6000,7000,8000]
# ```

# Four CPU-heavy jobs.

# ---

# # Start Timer

# ```python
# start_time = time.time()
# ```

# Stores start time.

# ---

# # Create Process Pool

# ```python
# with multiprocessing.Pool() as pool:
# ```

# Suppose your CPU has:

# ```text
# 8 Cores
# ```

# Python automatically creates worker processes.

# Think:

# ```text
# Worker 1
# Worker 2
# Worker 3
# Worker 4
# ...
# ```

# ---

# # Pool Map

# ```python
# results = pool.map(
#     computer_factorial,
#     numbers
# )
# ```

# Equivalent to:

# ```python
# computer_factorial(5000)
# computer_factorial(6000)
# computer_factorial(7000)
# computer_factorial(8000)
# ```

# but distributed across processes.

# ---

# # Visual Execution

# Without multiprocessing:

# ```text
# 5000!
#    ↓
# 6000!
#    ↓
# 7000!
#    ↓
# 8000!

# Total Time = A+B+C+D
# ```

# ---

# With multiprocessing:

# ```text
# Core1 → 5000!
# Core2 → 6000!
# Core3 → 7000!
# Core4 → 8000!

# Run Together
# ```

# Much faster.

# ---

# # What is Pool?

# Think of Pool as:

# ```text
# Team Manager
# ```

# Instead of creating:

# ```python
# p1
# p2
# p3
# p4
# ```

# manually,

# Pool automatically manages worker processes.

# ---

# # Interview Questions

# ### What is `multiprocessing.Pool()`?

# **Answer:**

# A Pool manages a collection of worker processes and distributes tasks among them.

# ---

# ### What does `pool.map()` do?

# **Answer:**

# Applies a function to every element in an iterable and distributes the work across multiple processes.

# Example:

# ```python
# pool.map(square, [1,2,3])
# ```

# Equivalent to:

# ```python
# square(1)
# square(2)
# square(3)
# ```

# executed in parallel.

# ---

# ### Why use multiprocessing for factorial?

# **Answer:**

# Factorial calculation is CPU-intensive. Multiprocessing allows the workload to be distributed across multiple CPU cores, improving performance.

# ---

# # Connection to Your Internship

# For your dish dataset project:

# ### Web Scraping

# ```text
# Waiting for website response
# ```

# Use:

# ```python
# ThreadPoolExecutor
# ```

# ### Image Processing

# ```text
# Resize 50,000 images
# ```

# Use:

# ```python
# multiprocessing.Pool()
# ```

# because image processing is CPU-heavy.

# ---

# ### Memory Trick

# ```text
# Waiting for Internet?
#       ↓
# Multithreading

# Heavy Computation?
#       ↓
# Multiprocessing
# ```

# This single rule solves 90% of interview questions on multithreading vs multiprocessing.
