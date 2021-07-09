import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    position = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    type_emp = models.CharField(max_length=200, blank=True, null=True)
    exp = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    pub_date = models.DateTimeField('date published',  blank=True, null=True)

    def __str__(self):
        return self.position + self.description
        
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now