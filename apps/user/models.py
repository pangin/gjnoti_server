import uuid

from django.db import models

# Create your models here.
from apps.keywords.models import Keyword
from apps.univ.models import Univ


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    chat_id = models.CharField(max_length=100, unique=True, null=True)
    keywords = models.ManyToManyField(Keyword, blank=True)
    univ = models.ForeignKey(Univ, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.chat_id
