from django.db import models

# Create your models here.
class FieldCategory(models.Model):
    field_id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class InterestTag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Job(models.Model):
    job_id = models.CharField(max_length=10, primary_key=True)
    job_name = models.CharField(max_length=100)
    job_description = models.TextField()
    emotive_copy= models.TextField()
    Soft_Skills = models.TextField()
    related_majors = models.TextField()
    entry_path = models.TextField()
    keyword_tags = models.CharField(max_length=200)
    recommend_reason = models.TextField()
    stem_category = models.CharField(max_length=100)
    related_tags = models.ManyToManyField(InterestTag)
    field = models.ForeignKey(FieldCategory, on_delete=models.SET_NULL, null=True)

    # 사용자편의성을 위함
    def __str__(self):
        return self.job_name