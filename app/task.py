from celery import shared_task
import time


@shared_task()
def text():
    time.sleep(15)
    return 'Hello world!'
