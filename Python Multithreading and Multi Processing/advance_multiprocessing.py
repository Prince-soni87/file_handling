# ### Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers = [1,2,3,4,5,6,7,8,9,11,2,3,12,14]

if __name__ == "__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)

    for result in results:
         print(result)




# Excellent question. The answer is:

# 👉 **Python automatically sets the value of `__name__`.**

# You do **not** set it yourself.

# ---

# ## Case 1: Run the file directly

# Suppose `app.py` contains:

# ```python
# print(__name__)
# ```

# You run:

# ```bash
# python app.py
# ```

# Python internally does:

# ```python
# __name__ = "__main__"
# ```

# Then executes:

# ```python
# print(__name__)
# ```

# Output:

# ```text
# __main__
# ```

# ---

# ## Case 2: Import the file

# ### app.py

# ```python
# print(__name__)
# ```

# ### main.py

# ```python
# import app
# ```

# When Python imports `app.py`, it internally does:

# ```python
# __name__ = "app"
# ```

# because the module name is `app`.

# Output:

# ```text
# app
# ```

# ---

# ## How Python Knows?

# Imagine you run:

# ```bash
# python app.py
# ```

# Python says:

# ```text
# I started with app.py
# So app.py is the MAIN file.
# ```

# Therefore:

# ```python
# __name__ = "__main__"
# ```

# ---

# But if you run:

# ```bash
# python main.py
# ```

# and inside `main.py`:

# ```python
# import app
# ```

# Python says:

# ```text
# main.py started first.
# app.py was imported later.
# ```

# So:

# ```python
# # inside main.py
# __name__ = "__main__"

# # inside app.py
# __name__ = "app"
# ```

# ---

# ## Try This Yourself

# ### app.py

# ```python
# print("app.py __name__ =", __name__)
# ```

# ### main.py

# ```python
# print("main.py __name__ =", __name__)

# import app
# ```

# Run:

# ```bash
# python main.py
# ```

# Output:

# ```text
# main.py __name__ = __main__
# app.py __name__ = app
# ```

# See?

# * `main.py` started execution → `__name__ = "__main__"`
# * `app.py` was imported → `__name__ = "app"`

# ---

# ### Visual Memory Trick

# ```text
# python app.py
#        │
#        ▼
# app.py started first
#        │
#        ▼
# __name__ = "__main__"
# ```

# ```text
# python main.py
#        │
#        ▼
# main.py started first
#        │
#        ▼
# __name__ = "__main__"

# app.py imported
#        │
#        ▼
# __name__ = "app"
# ```

# So `if __name__ == "__main__":` is simply checking:

# ```text
# "Did Python start execution from this file?"
# ```

# * Yes → Run the block.
# * No (imported) → Skip the block.


