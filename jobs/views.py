from django.shortcuts import render
from django.shortcuts import get_object_or_404
from jobs.models import Job

# Create your views here.
# views.py


def job_detail(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})