import os
import sys

def run_server():

    print("RUN celery")
    if len(sys.argv) > 2:
        port = sys.argv[2]
    else:
        port = 5100

    a = f"python -m celery -A tasks.app flower --port={port}"
    print(a)
    os.system(a)


if __name__ == "__main__":
    run_server()
