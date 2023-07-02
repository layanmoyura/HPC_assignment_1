import random
import numpy as np
from mpi4py import MPI
import time

time_start = time.time()

# Initialize MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

num_students = 50
num_subjects = 4

marks = np.random.randint(0, 101, size=(num_students,num_subjects))
local_data = marks[:,rank]
local_average = np.mean(local_data)

if rank == 0:
    print(f"Average of Mathematics: >> {local_average}")
elif rank == 1:
    print(f"Average of English: >> {local_average}")
elif rank == 2: 
    print(f"Average of Data Structures and Algorithms: >> {local_average}")
elif rank == 3:
    print(f"Average of High Performance Computing: >> {local_average}")
else:
    print("Error: Rank is not in range 0-3")


time_end = time.time()
print(f"Time taken: {time_end-time_start} seconds")
