from mpi4py import MPI
import random
from prettytable import PrettyTable

# Initialize MPI
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Number of students and subjects
num_students = 50
num_subjects = 4

# Generate random marks for all subjects for each process
marks = []
for _ in range(num_students):
    student_marks = [random.randint(0, 100) for _ in range(num_subjects)]
    marks.append(student_marks)

# Scatter marks to all processes
local_marks = comm.Scatter(marks, root=0)

# Calculate the sum of marks for each subject locally
local_sums = [sum(subject_marks) for subject_marks in zip(*local_marks)]

# Reduce the subject sums to get the total sums on the root process
total_sums = comm.reduce(local_sums, op=MPI.SUM, root=0)

# Calculate the average marks per subject on the root process
if rank == 0:
    math_sum, english_sum, dsa_sum, hpc_sum = total_sums
    math_average = math_sum / num_students
    english_average = english_sum / num_students
    dsa_average = dsa_sum / num_students
    hpc_average = hpc_sum / num_students
else:
    math_average = english_average = dsa_average = hpc_average = None

# Broadcast the average marks to all processes
math_average = comm.bcast(math_average, root=0)
english_average = comm.bcast(english_average, root=0)
dsa_average = comm.bcast(dsa_average, root=0)
hpc_average = comm.bcast(hpc_average, root=0)

# Create the marks table on each process
marks_table = PrettyTable()
marks_table.field_names = ["Student No.", "Mathematics", "English", "Data Structures and Algorithms", "High Performance Computing"]
for student, student_marks in enumerate(local_marks, start=1):
    marks_table.add_row([student] + student_marks)

# Print the marks table on each process
print(f"Process {rank}: Students' Marks:")
print(marks_table)

# Create the average marks table on the root process
if rank == 0:
    average_table = PrettyTable()
    average_table.field_names = ["Subject", "Average Marks"]
    average_table.add_row(["Mathematics", math_average])
    average_table.add_row(["English", english_average])
    average_table.add_row(["Data Structures and Algorithms", dsa_average])
    average_table.add_row(["High Performance Computing", hpc_average])

    # Print the average marks table on the root process
    print("\nAverage marks per subject:")
    print(average_table)
