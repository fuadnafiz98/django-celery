from django.db import models
from uuid import uuid4


class Youtube(models.Model):
    objects = models.Manager()

    id = models.UUIDField(default=uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name}"


class Content(models.Model):
    objects = models.Manager()

    id = models.UUIDField(default=uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=100)
    payment_rate = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
    )
    content_quote = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        default=0,
    )
    content_approved = models.DateTimeField(default=None, null=True, blank=True)

    youtube = models.ForeignKey(Youtube, on_delete=models.SET_NULL, null=True, related_name='youtube')

    def __str__(self) -> str:
        return f"{self.name}"
