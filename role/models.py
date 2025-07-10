from django.db import models
from jobs.models import Job

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    role_title = models.CharField(max_length=255)
    short_bio = models.TextField()
    quote = models.TextField()
    original_url = models.URLField()

    def __str__(self):
        return self.role_name
