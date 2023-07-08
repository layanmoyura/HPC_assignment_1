import time
import subprocess

start_time = time.time()
subprocess.run(["python3", "part_1.py"])
part_1_time = time.time() - start_time
print("\n")

start_time = time.time()
subprocess.run(["mpirun","-np","4","python3","part_2.py"])
part_2_time = time.time() - start_time
print("\n")

speedup_ratio = part_1_time / part_2_time

print("Part 1 Execution Time: {:.2f} seconds".format(part_1_time))
print("Part 2 Execution Time: {:.2f} seconds".format(part_2_time))
print("Speedup Ratio: {:.2f}".format(speedup_ratio))
print("\n")

start_time = time.time()
subprocess.run(["python3", "part1_with_np.py"])
part_1_time = time.time() - start_time
print("\n")

start_time = time.time()
subprocess.run(["mpirun","-np","4","python3","part2_with_np.py"])
part_2_time = time.time() - start_time
print("\n")

speedup_ratio = part_1_time / part_2_time

print("Part 1 Execution Time (with NumPy): {:.2f} seconds".format(part_1_time))
print("Part 2 Execution Time (with NumPy): {:.2f} seconds".format(part_2_time))
print("Speedup Ratio (with NumPy): {:.2f}".format(speedup_ratio))
