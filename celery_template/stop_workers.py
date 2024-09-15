import os
import sys

sys.path.append(os.getcwd())

import json
import os
import signal

try:
    with open("previous_workers.txt", "r") as f:
        pre_workers = [w.strip() for w in f.readlines()]

except:
    pre_workers = []


def cold_stop(pre_workers):
    """
    Stop all Celery worker processes gracefully.

    Args:
        pre_workers (list): List of worker names.
    """
    for worker in pre_workers:
        print(f"Stopping Celery worker {worker}")
        os.system(f"pkill -f {worker}")

    command = "celery -A tasks purge -f & redis-cli FLUSHALL"
    os.system(command)


def warm_stop(pre_workers):
    """
    Perform a cold stop for Celery workers.

    Args:
        pre_workers (list): List of worker names.
    """
    print("Performing cold stop...")
    stop_command = "celery multi stop "
    for worker in pre_workers:
        stop_command += f"{worker} "
    stop_command += '--pidfile="pids/%n.pid"'
    if len(pre_workers) > 0:
        os.system(stop_command)


if __name__ == "__main__":
    exit_choice = input("cold stop or warm stop (1 or 2): ")

    if exit_choice == "1":
        cold_stop(pre_workers=pre_workers)
    else:
        warm_stop(pre_workers=pre_workers)
