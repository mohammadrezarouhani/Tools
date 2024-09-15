import os
import sys
import random
from datetime import datetime


def run_worker(worker_name, rand_moj):
    dt = datetime.now().strftime("%d-%b-%H-%M-%S")
    log_file = Path(f"./logs/{dt}-%n-{rand_moj}.log")
    manger = f'celery multi restart {worker_name} -A tasks -l debug -Q:{worker_name} {worker_name} --autoscale=1,1 --pidfile=pids/%n.pid --logfile="{log_file}"'
    os.system(manger)


if __name__ == "__main__":
    worker_name = ["create_account"]

    rand_imj = random.choice(
        [
            "🔥",
            "✨",
            "📝",
            "🚀",
            "✅",
            "📄",
            "💥",
            "💡",
            "💬",
            "🗃️",
            "📸",
            "🔍️",
            "🏷️",
            "🚩",
            "💫",
        ]
    )

    for name in worker_name:
        run_worker(name, rand_imj)
