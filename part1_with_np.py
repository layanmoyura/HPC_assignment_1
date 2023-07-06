import numpy as np

num_students = 20000000
num_subjects = 4
marks = np.random.randint(0, 101, size=(num_subjects,num_students))
subjects = ["Mathematics","English","Data Structures and Algorithms","High Performance Computing"]

for subject_index in range(num_subjects):
    local_data = marks[subject_index,:]
    local_average = np.average(local_data)
    subject = subjects[subject_index]
    print(f"Average of {subject}: >> {local_average}")
