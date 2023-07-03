# HPC_assignment_1
Problem: Write an MPI program to calculate the average grades for each subject of 50 students. Use a sequential program and an MPI program with 4 processes for faster calculation. Increase the number of students to 10,000 or 100,000 to observe performance improvement. Chart the speed-up by varying the number of students.

## Python

Create a virtual environment

```bash
python3 -m venv mpi_env
source mpi_env/bin/activate
pip install mpi4py
```

## Run Examples

### Python

```bash
mpirun -n 4 python3 hello_world.py
```
