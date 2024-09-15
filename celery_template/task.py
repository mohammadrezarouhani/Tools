from .config import app


@app.task(
    name="tasks.test",
    bind=True,
    max_retries=10,
    time_limit=12 * 60,
    soft_time_limit=10 * 60,
)
def test(self):
    print("excuted")