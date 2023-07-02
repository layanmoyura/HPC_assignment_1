import random
import numpy as np
from prettytable import PrettyTable
from mpi4py import MPI

num_students = 50
num_subjects = 4

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size_1 = comm.Get_size()

marks = np.random.randint(0, 101, size=(num_students, num_subjects))

local_marks = np.empty((num_students, num_subjects), dtype=int)
comm.Scatter(marks, local_marks, root=0)
subject_sums = np.sum(local_marks, axis=0)
local_averages = np.mean(local_marks, axis=0)

global_averages = np.zeros_like(local_averages)
comm.Reduce(local_averages, global_averages, op=MPI.SUM, root=0)

if rank == 0:
    subject_averages = global_averages/size_1

    marks_table = PrettyTable()
    marks_table.field_names = ["Student No.", "Mathematics", "English", "Data Structures and Algorithms", "High Performance Computing"]
    for student in range(num_students):
        marks_table.add_row([student+1] + marks[student].tolist())

    average_table = PrettyTable()
    average_table.field_names = ["Subject", "Average Marks"]
    average_table.add_row(["Mathematics", subject_averages[0]])
    average_table.add_row(["English", subject_averages[1]])
    average_table.add_row(["Data Structures and Algorithms", subject_averages[2]])
    average_table.add_row(["High Performance Computing", subject_averages[3]])

    print("Students' Marks:")
    print(marks_table)
    print("\nAverage marks per subject:")
    print(average_table)
