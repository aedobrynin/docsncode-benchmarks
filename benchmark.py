import subprocess
import sys
import shutil
import time

EXECUTION_TRIES = 10

# Returns execution time (sec.)
def run_docsncode(path: str, cache_type: str) -> float:
    result_path = f'{path}-result'
    try:
        shutil.rmtree(result_path)
    except FileNotFoundError:
        pass

    command = f"./docsncode {path} {result_path} --force-rebuild --cache {cache_type}"

    start_time = time.time()

    subprocess.run(command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python3 benchmark.py <path-to-project-dir> [cache-type (none, modtime, hash)]")
        sys.exit(1)

    path = sys.argv[1]
    execution_times = []

    cache_type = 'modtime'
    if len(sys.argv) == 3:
        cache_type = sys.argv[2]

    for _ in range(EXECUTION_TRIES):
        execution_time = run_docsncode(path, cache_type)
        execution_times.append(execution_time)
        print('Execution try finished, execution_time:', execution_time, 's.')

    min_execution_time = min(execution_times)
    avg_execution_time = sum(execution_times) / EXECUTION_TRIES
    max_execution_time = max(execution_times)

    print(f"Min execution time: {min_execution_time:.10f} seconds")
    print(f"Avg execution time: {avg_execution_time:.10f} seconds")
    print(f"Max execution time: {max_execution_time:.10f} seconds")
