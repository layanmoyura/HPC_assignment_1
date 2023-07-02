import random
import numpy as np
from mpi4py import MPI
import time

time_start = time.time()

num_students = 500000
num_subjects = 4
marks = np.random.randint(0, 101, size=(num_students,num_subjects))
subjects = ["Mathematics","English","Data Structures and Algorithms","High Performance Computing"]

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

local_data = marks[:,rank]
local_average = np.mean(local_data)
subject = subjects[rank]
print(f"Average of {subject}: >> {local_average}")

comm.Barrier()

if rank == 0:
    time_end = time.time()
    print(f"Time taken: {time_end-time_start} seconds")



