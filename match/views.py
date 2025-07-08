from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import InterestTag, Job

# match/ 첫 화면 (아무것도 없음. 임시 화면)
def match_home(request):
    return HttpResponse("Match 홈")

# http://127.0.0.1:8000/match/choose 화면 view
def choose_interest_view(request):
    tags = InterestTag.objects.all()
    return render(request, 'match/m_choose.html', {'tags': tags})

# http://127.0.0.1:8000/match/job/ 화면 view
def job_select_view(request):
    tag_ids = request.GET.getlist('tag_ids')

    # 관심사 선택되지 않았을 때의 처리 (버튼이 클릭되지 않도록 한다면, JS로 처리해야 함)
    if not tag_ids:
        return render(request, 'match/m_job.html', {
            'jobs': [],
            'tags': [],
            'message': '선택된 관심사가 없습니다.'
        })

    tags = InterestTag.objects.filter(tag_id__in=tag_ids)
    jobs = Job.objects.filter(related_tags__tag_id__in=tag_ids).distinct()

    return render(request, 'match/m_job.html', {
        'tags': tags,
        'jobs': jobs,
        'message': None if jobs else '이 관심사에 해당하는 직무가 없습니다.'
    })

# http://127.0.0.1:8000/match/job_detail/ 의 view (선택한 직무 상세보기)
def job_detail_view(request):
    job_id = request.GET.get('job_id')
    job = get_object_or_404(Job, job_id=job_id)
    return render(request, 'match/m_job_detail.html', {'job': job})
