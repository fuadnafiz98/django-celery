from __future__ import absolute_import, unicode_literals

from celery import shared_task
from time import sleep

list = [1, 2, 3, 4, 5, 6]


@shared_task()
def multiply(x, y):
    for item in list:
        print(f"running item {item}")
        sleep(2)
    return x * y
