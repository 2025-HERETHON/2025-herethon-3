from django.shortcuts import render
from django.shortcuts import get_object_or_404
from jobs.models import Job, UserLikedJob
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# views.py

# 직무 상세 보기
def job_detail(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    return render(request, 'jobs/job_detail.html', {'job': job})

# 상세 직무 하트 눌러서 저장하기
@login_required
def like_job_view(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    user = request.user

    liked, created = UserLikedJob.objects.get_or_create(user=user, job=job)
    if not created:
        liked.delete()
        return JsonResponse({"status": "unliked"})

    return JsonResponse({"status": "liked"})
