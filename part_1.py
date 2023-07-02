import random
import numpy as np
import time

time_start = time.time()

num_students = 5000
num_subjects = 4
marks = np.random.randint(0, 101, size=(num_students,num_subjects))
subjects = ["Mathematics","English","Data Structures and Algorithms","High Performance Computing"]

for subject_index in range(num_subjects):
    local_data = marks[:,subject_index]
    local_average = np.mean(local_data)
    subject = subjects[subject_index]
    print(f"Average of {subject}: >> {local_average}")

time_end = time.time()

print(f"\nTime taken: {time_end-time_start} seconds")
