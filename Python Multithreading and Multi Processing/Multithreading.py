# import time

# def print_numbers():
#     for i in range(5):
#         print(f"Number:{i}")

# def print_letter():
#     for letter in "abcde":
#         print(f"Letter: {letter}")

# t = time.time()

# print_numbers()
# print_letter()

# finished_time = time.time() - t

# print(finished_time)




# import time

# def print_numbers():
#     for i in range(5):
#         time.sleep(2)
#         print(f"Number:{i}")

# def print_letter():
#     for letter in "abcde":
#         time.sleep(2)
#         print(f"Letter: {letter}")

# t = time.time()

# print_numbers()
# print_letter()

# finished_time = time.time() - t

# print(finished_time)

# # create 2 threads

# t1 = threading.Thread(target=print_numbers)
# t2 = threading.Thread(target=print_letter)

# t = time.time()

# # start the thread
# t1.start()
# t2.start()

# ### Wait for the threads to complete

# t1.join()
# t2.join()

# finished_time = time.time() - t
# print(finished_time)



import threading
import time

def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letter():
    for letter in "abcde":
        print(f"Letter: {letter}")
        time.sleep(1)

# Create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

# Start timer
t = time.time()

# Start threads
t1.start()
t2.start()

# Wait for threads to finish
t1.join()
t2.join()

# Calculate execution time
finished_time = time.time() - t

print(f"\nExecution Time: {finished_time:.2f} seconds")



