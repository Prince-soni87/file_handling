### Multithreading With Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number :{number}"

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)




# ## Extracted Code

# ```python id="83m9di"
# ### Multithreading With Thread Pool Executor

# from concurrent.futures import ThreadPoolExecutor
# import time

# def print_number(number):
#     time.sleep(1)
#     return f"Number :{number}"

# numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

# with ThreadPoolExecutor(max_workers=3) as executor:
#     results = executor.map(print_number, numbers)

# for result in results:
#     print(result)
# ```

# ---

# # What is ThreadPoolExecutor?

# Before this, you created threads manually:

# ```python id="nax6e5"
# t1 = threading.Thread(...)
# t2 = threading.Thread(...)
# t3 = threading.Thread(...)
# ```

# Imagine you have:

# ```python id="jb7vxb"
# 100 tasks
# ```

# Creating 100 threads manually is difficult.

# Instead use:

# ```python id="3zhbr7"
# ThreadPoolExecutor
# ```

# It automatically manages threads for you.

# ---

# # Simple Real-Life Example

# Imagine a restaurant.

# ### Without Thread Pool

# You hire workers manually:

# ```text id="t84l0d"
# Worker 1
# Worker 2
# Worker 3
# ...
# Worker 100
# ```

# Difficult to manage.

# ---

# ### With Thread Pool

# Manager says:

# ```text id="rqj4x6"
# Keep only 3 workers.
# Give them tasks one by one.
# ```

# This is exactly what:

# ```python id="jzmsl4"
# ThreadPoolExecutor(max_workers=3)
# ```

# does.

# ---

# # Line-by-Line Explanation

# ## Import

# ```python id="m1c0sn"
# from concurrent.futures import ThreadPoolExecutor
# ```

# Imports Python's thread pool implementation.

# ---

# ## Function

# ```python id="h3j3m0"
# def print_number(number):
# ```

# Receives a number.

# ---

# ### Simulate Work

# ```python id="6h6vns"
# time.sleep(1)
# ```

# Pretend the task takes 1 second.

# ---

# ### Return Result

# ```python id="dhh96r"
# return f"Number :{number}"
# ```

# Example:

# ```python id="iij25t"
# print_number(5)
# ```

# returns:

# ```text id="edvqj5"
# Number :5
# ```

# ---

# ## Input Data

# ```python id="h7p1nv"
# numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]
# ```

# 13 tasks.

# ---

# ## Create Thread Pool

# ```python id="5p2qkk"
# with ThreadPoolExecutor(max_workers=3) as executor:
# ```

# Creates:

# ```text id="vhivku"
# Thread 1
# Thread 2
# Thread 3
# ```

# Only 3 threads exist.

# ---

# ## Map Tasks

# ```python id="jhf4of"
# results = executor.map(print_number, numbers)
# ```

# Equivalent to:

# ```python id="k44g1y"
# print_number(1)
# print_number(2)
# print_number(3)
# ...
# ```

# but distributed among 3 threads.

# ---

# ### Execution Example

# ```text id="u3jh5l"
# Thread 1 -> Number 1
# Thread 2 -> Number 2
# Thread 3 -> Number 3
# ```

# After completion:

# ```text id="dr4r0l"
# Thread 1 -> Number 4
# Thread 2 -> Number 5
# Thread 3 -> Number 6
# ```

# and so on.

# ---

# ## Print Results

# ```python id="s5t3wc"
# for result in results:
#     print(result)
# ```

# Output:

# ```text id="jlwmuh"
# Number :1
# Number :2
# Number :3
# Number :4
# ...
# ```

# ---

# # Why Use ThreadPoolExecutor?

# ### Manual Threads

# ```python id="ktp6a5"
# t1 = Thread(...)
# t2 = Thread(...)
# t3 = Thread(...)
# ```

# Problems:

# ```text id="qjl1ja"
# Too much code
# Hard to manage
# ```

# ---

# ### ThreadPoolExecutor

# ```python id="bwy63x"
# ThreadPoolExecutor(max_workers=3)
# ```

# Benefits:

# ```text id="fmxwdd"
# Automatic thread management
# Reusable threads
# Cleaner code
# Better scalability
# ```

# ---

# # What Does `max_workers=3` Mean?

# ```python id="gt58xy"
# ThreadPoolExecutor(max_workers=3)
# ```

# Means:

# ```text id="j9eky0"
# Maximum 3 threads can run simultaneously
# ```

# ---

# ### Example

# Tasks:

# ```text id="esw1v6"
# 1 2 3 4 5 6 7 8 9
# ```

# Workers:

# ```text id="r6k8e9"
# Worker1
# Worker2
# Worker3
# ```

# Execution:

# ```text id="e7j21p"
# Round 1:
# 1 2 3

# Round 2:
# 4 5 6

# Round 3:
# 7 8 9
# ```

# ---

# # Interview Questions

# ### Q1. What is ThreadPoolExecutor?

# **Answer:**

# `ThreadPoolExecutor` is a high-level API from the `concurrent.futures` module that manages a pool of worker threads and executes tasks concurrently.

# ---

# ### Q2. Why use ThreadPoolExecutor instead of creating threads manually?

# **Answer:**

# It automatically creates, manages, and reuses threads, resulting in cleaner and more scalable code.

# ---

# ### Q3. What does `max_workers` mean?

# **Answer:**

# It specifies the maximum number of worker threads that can execute tasks concurrently.

# Example:

# ```python id="8n0z6r"
# ThreadPoolExecutor(max_workers=3)
# ```

# allows at most 3 threads to run simultaneously.

# ---

# ### Q4. What does `executor.map()` do?

# **Answer:**

# It applies a function to every item in an iterable and executes the tasks concurrently using the thread pool.

# ---

# # IQ 1000 Memory Trick

# ```text id="dz5lxh"
# Few Tasks
#     ↓
# Thread()

# Many Tasks
#     ↓
# ThreadPoolExecutor()

# CPU Heavy
#     ↓
# ProcessPoolExecutor()

# I/O Heavy
#     ↓
# ThreadPoolExecutor()
# ```

# ### One-Line Interview Answer

# > `ThreadPoolExecutor` manages a pool of worker threads and executes multiple tasks concurrently, making multithreaded programs easier to write and maintain.
