from django.contrib import admin

# Register your models here.
from apps.keywords.models import Keyword
admin.site.register(Keyword)
