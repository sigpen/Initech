from django.conf import settings
from django.db import models

class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user')