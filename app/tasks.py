from __future__ import absolute_import, unicode_literals
from django.db.transaction import atomic

from celery import shared_task
from time import sleep

_list = [1, 2, 3, 4, 5, 6]


@shared_task()
@atomic
def send_email(item):
  print(f"printing mail...{item}")


@shared_task()
def multiply(x, y):
  for i, item in enumerate(_list):
    send_email.apply_async(kwargs={"item": item}, countdown=(i + 1) * 30)
