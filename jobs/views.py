from django.shortcuts import render
from django.shortcuts import get_object_or_404
from jobs.models import Job, UserLikedJob
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from match.models import Job
from django.utils import timezone

# Create your views here.
# views.py

# 직무 상세 보기
def job_detail(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    job.last_viewed_at = timezone.now()
    job.save()
    # 최근 본 직무 저장 (세션에 job_id만 저장)
    recent_jobs = request.session.get('recent_jobs', [])

    # 중복 제거 및 현재 job_id 삽입
    if job_id in recent_jobs:
        recent_jobs.remove(job_id)
    recent_jobs.insert(0, job_id)

    # 최근 본 직무는 최대 3개만 유지
    request.session['recent_jobs'] = recent_jobs[:3]
    print("✅ 현재 세션 viewed_jobs:", recent_jobs)  # 디버깅용
    
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
