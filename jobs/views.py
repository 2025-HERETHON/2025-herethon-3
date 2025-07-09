from django.shortcuts import render
from django.shortcuts import get_object_or_404
from jobs.models import Job

# Create your views here.
# views.py
def test_job_list(request):
    jobs = Job.objects.all()[:5]  # 앞 5개만 테스트
    return render(request, 'jobs/jobs_by_tag.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})