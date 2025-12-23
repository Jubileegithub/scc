import subprocess
import time
import sys

graph = sys.argv[1]
start = sys.argv[2]
procs = int(sys.argv[3])

start_time = time.time()

subprocess.run([
    "mpirun", "-np", str(procs),
    "python", "bfs_mpi.py", graph, start
])

end_time = time.time()
print("Processes:", procs)
print("Time:", end_time - start_time)
