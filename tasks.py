import celery

app = celery.Celery('example')


@app.task
def add(x, y):
    return (x + y) * x


app.conf.update(BROKER_URL='redis://',
                CELERY_RESULT_BACKEND='redis://')
