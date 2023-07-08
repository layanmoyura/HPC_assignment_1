import numpy as np
from mpi4py import MPI

num_students = 2000000
num_subjects = 4
marks = np.random.randint(0, 101, size=(num_subjects,num_students))
subjects = ["Mathematics","English","Data Structures and Algorithms","High Performance Computing"]

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

local_data = marks[rank,:]
local_average = np.average(local_data)
subject = subjects[rank]
print(f"Average of {subject}: >> {local_average} rank:{rank}")


