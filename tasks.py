import celery

app = celery.Celery('example')


@app.task
def add(x, y):
    return (x + y) * x


import os

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
