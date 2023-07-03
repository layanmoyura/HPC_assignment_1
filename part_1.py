import random
import numpy as np
#import time

#time_start = time.time()

num_students = 1500000
num_subjects = 4
marks = np.random.randint(0, 101, size=(num_students,num_subjects))
subjects = ["Mathematics","English","Data Structures and Algorithms","High Performance Computing"]

for subject_index in range(num_subjects):
    local_data = marks[:,subject_index]
    local_average = 0
    for student_index in range(num_students):
        local_average += local_data[student_index]
    local_average /= num_students
    subject = subjects[subject_index]
    print(f"Average of {subject}: >> {local_average}")

#time_end = time.time()

#print(f"\nTime taken: {time_end-time_start} seconds")
#with open("serial_program.txt", "a") as text_file:
    #text_file.write(f"\nTime taken: {time_end-time_start} seconds")
    #text_file.write(f" Number of students: {num_students}")