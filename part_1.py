import random
from prettytable import PrettyTable

math_sum = 0
english_sum = 0
dsa_sum = 0
hpc_sum = 0
marks_table = PrettyTable()
marks_table.field_names = ["Student No.","Mathematics","English","Data Structures and Algorithms","High Performance Computing"]

for student in range(1, 51):

    math_marks = random.randint(0, 100)
    english_marks = random.randint(0, 100)
    dsa_marks = random.randint(0, 100)
    hpc_marks = random.randint(0, 100)

    math_sum += math_marks
    english_sum += english_marks
    dsa_sum += dsa_marks
    hpc_sum += hpc_marks

    marks_table.add_row([student, math_marks, english_marks, dsa_marks, hpc_marks])


math_average = math_sum/50
english_average = english_sum/50
dsa_average = dsa_sum/50
hpc_average = hpc_sum/50

average_table = PrettyTable()
average_table.field_names = ["Subject","Average Marks"]
average_table.add_row(["Mathematics",math_average])
average_table.add_row(["English",english_average])
average_table.add_row(["Data Structures and Algorithms",dsa_average])
average_table.add_row(["High Performance Computing",hpc_average])

print("Students' Marks:")
print(marks_table)
print("\nAverage marks per subject:")
print(average_table)
