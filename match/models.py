from django.db import models
from django.conf import settings

class InterestTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.tag_name
    

# Job model 생성
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=100)
    job_description = models.TextField()
    related_majors = models.TextField()
    entry_path = models.TextField()
    keyword_tags = models.TextField()
    recommend_reason = models.TextField()
    stem_category = models.CharField(max_length=100)
    field_id = models.CharField(max_length=10)
    field_name = models.CharField(max_length=100)
    
    # ManyToMany: 여러 직무가 여러 관심사에 연결됨
    related_tags = models.ManyToManyField(InterestTag)

    def __str__(self):
        return self.job_name
    

# UserSelectedTag model 생성
class UserSelectedTag(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tag = models.ForeignKey(InterestTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.tag.tag_name}"