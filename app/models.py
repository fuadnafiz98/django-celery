from django.db import models
from uuid import uuid4


class BigQuery(models.Model):
    objects = models.Manager()

    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"
