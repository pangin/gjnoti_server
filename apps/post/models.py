import uuid

from django.db import models

# Create your models here.
from apps.univ.models import Univ


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=150)
    univ = models.ForeignKey(Univ, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.post_title
