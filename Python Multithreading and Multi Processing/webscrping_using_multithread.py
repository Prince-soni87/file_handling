# This example is actually very close to the **web scraping project you're doing in your internship**, so let's connect it to your real work.

# ---

# # What problem are we solving?

# Suppose you have 3 websites:

# ```python
# urls = [
#     "https://python.langchain.com/v0.2/docs/introduction/",
#     "https://python.langchain.com/v0.2/docs/concepts/",
#     "https://python.langchain.com/v0.2/docs/tutorials/"
# ]
# ```

# Without multithreading:

# ```python
# for url in urls:
#     requests.get(url)
# ```

# Execution:

# ```text
# Download URL 1  -> Wait 2 sec
# Download URL 2  -> Wait 2 sec
# Download URL 3  -> Wait 2 sec

# Total = 6 sec
# ```

# ---

# # With Multithreading

# Create 3 workers:

# ```text
# Thread 1 -> URL 1
# Thread 2 -> URL 2
# Thread 3 -> URL 3
# ```

# Execution:

# ```text
# Thread 1 -> Download URL 1
# Thread 2 -> Download URL 2
# Thread 3 -> Download URL 3
# ```

# All start together.

# ```text
# Total ≈ 2 sec
# ```

# instead of 6 sec.

# ---

# # Understanding Your Code

# ## Function

# ```python
# def fetch_content(url):
# ```

# Receives one URL.

# Example:

# ```python
# fetch_content("https://python.langchain.com")
# ```

# ---

# ## Send Request

# ```python
# response = requests.get(url)
# ```

# Think:

# ```text
# Browser opens URL
# Downloads webpage
# ```

# ---

# ## Parse HTML

# ```python
# soup = BeautifulSoup(response.content, 'html.parser')
# ```

# Converts:

# ```html
# <html>
#    <body>Hello</body>
# </html>
# ```

# into a Python object that can be searched.

# ---

# ## Print Result

# ```python
# print(f"Fetched {len(soup.text)} characters from {url}")
# ```

# Example:

# ```text
# Fetched 10523 characters from https://python.langchain.com
# ```

# ---

# # Why `threads=[]`?

# ```python
# threads = []
# ```

# Empty list.

# Used to store all created threads.

# Think:

# ```text
# Worker List

# []
# ```

# ---

# # Loop Through URLs

# ```python
# for url in urls:
# ```

# One by one:

# ```text
# URL1
# URL2
# URL3
# ```

# ---

# # Create Thread

# ```python
# thread = threading.Thread(
#     target=fetch_content,
#     args=(url,)
# )
# ```

# For URL1:

# ```python
# threading.Thread(
#     target=fetch_content,
#     args=("URL1",)
# )
# ```

# Meaning:

# ```text
# Create worker
# Run fetch_content(URL1)
# ```

# ---

# # Why `(url,)` ?

# This is an interview favorite.

# Wrong:

# ```python
# args=(url)
# ```

# Python thinks:

# ```text
# Just a string
# ```

# Correct:

# ```python
# args=(url,)
# ```

# Comma makes it a tuple.

# ```python
# ("URL1",)
# ```

# ---

# # Store Thread

# ```python
# threads.append(thread)
# ```

# Now:

# ```text
# threads = [Thread1]
# ```

# Then:

# ```text
# threads = [Thread1, Thread2]
# ```

# Then:

# ```text
# threads = [Thread1, Thread2, Thread3]
# ```

# ---

# # Start Thread

# ```python
# thread.start()
# ```

# This is where work actually begins.

# ```text
# Thread1 starts downloading URL1
# Thread2 starts downloading URL2
# Thread3 starts downloading URL3
# ```

# ---

# # Wait for Completion

# ```python
# for thread in threads:
#     thread.join()
# ```

# Meaning:

# ```text
# Wait for Thread1
# Wait for Thread2
# Wait for Thread3
# ```

# Only after all finish:

# ```python
# print("All web pages fetched")
# ```

# runs.

# ---

# # Why is this useful for YOUR project?

# You're scraping:

# ```text
# Zomato
# Swiggy
# Wikipedia
# NDTV Food
# Tourism websites
# ```

# Without threads:

# ```text
# Page1 -> wait
# Page2 -> wait
# Page3 -> wait
# ```

# Very slow.

# With threads:

# ```text
# Page1
# Page2
# Page3
# Page4
# Page5
# ```

# download simultaneously.

# This is why **web scraping is one of the best use cases for multithreading**.

# ---

# # Interview Question

# ### Why is multithreading good for web scraping?

# **Answer:**

# Web scraping is an I/O-bound task because most of the time is spent waiting for server responses. Multithreading allows multiple requests to be sent concurrently, reducing overall execution time.

# ### Why do we use `join()`?

# **Answer:**

# To ensure the main program waits until all threads finish execution before proceeding.

# ### Why use `args=(url,)`?

# **Answer:**

# Because `args` expects a tuple. For a single argument tuple, a trailing comma is required.

# ---

# ### One-line Summary

# ```text
# Web Scraping = Waiting for Internet Response
# Waiting = I/O Bound
# I/O Bound = Multithreading is best
# ```

# This is exactly the technique used in high-speed scrapers and crawlers.

import threading
import requests
from bs4 import BeautifulSoup
import time

# List of URLs to scrape
urls = [
    "https://python.langchain.com/v0.2/docs/introduction/",
    "https://python.langchain.com/v0.2/docs/concepts/",
    "https://python.langchain.com/v0.2/docs/tutorials/"
]

# Function to fetch webpage content
def fetch_content(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")

            print(
                f"Fetched {len(soup.text)} characters from {url}"
            )
        else:
            print(
                f"Failed to fetch {url} | Status Code: {response.status_code}"
            )

    except Exception as e:
        print(f"Error fetching {url}: {e}")


# Start timer
start_time = time.time()

# Create thread list
threads = []

# Create and start threads
for url in urls:
    thread = threading.Thread(
        target=fetch_content,
        args=(url,)
    )

    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("\nAll web pages fetched")

# Execution time
end_time = time.time()

print(f"Execution Time: {end_time - start_time:.2f} seconds")
