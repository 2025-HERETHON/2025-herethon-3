from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import InterestTag, Job , UserSelectedTag
from django.contrib.auth.decorators import login_required
from match.models import UserSelectedTag
from django.utils.http import urlencode


# match/ 첫 화면 (아무것도 없음. 임시 화면)
@login_required
def match_home(request):
    return HttpResponse("Match 홈")

# http://127.0.0.1:8000/match/choose 화면 view
@login_required
def choose_interest_view(request):
    if request.method == 'POST':
        selected_tag_ids = request.POST.getlist('tag_ids')  # checkbox name이 'tag_ids'일 때
        print("🔍 선택된 tag_ids:", selected_tag_ids)


        # 이전 선택 삭제 (선택 1회만 허용 또는 업데이트하려면 필요)
        UserSelectedTag.objects.filter(user=request.user).delete()

        # 새 선택 저장
        for tag_id in selected_tag_ids:
            tag = get_object_or_404(InterestTag, tag_id=tag_id)
            UserSelectedTag.objects.create(user=request.user, tag=tag)

        query_string = urlencode([('tag_ids', tag_id) for tag_id in selected_tag_ids])
        return redirect(f'/match/job/?{query_string}')

    # GET 요청: 관심사 선택 화면 보여주기
    tags = InterestTag.objects.all()
    print("✅ InterestTag 총 개수:", tags.count()) # 디버깅용 출력
    
    return render(request, 'match/m_choose.html', {'tags': tags})

# http://127.0.0.1:8000/match/job/ 화면 view
@login_required
def job_select_view(request):
    tag_ids = request.GET.getlist('tag_ids')

    # 관심사 선택되지 않았을 때의 처리 (버튼이 클릭되지 않도록 한다면, JS로 처리해야 함)
    if not tag_ids:
        return render(request, 'match/m_job.html', {
            'jobs': [],
            'tags': [],
            'message': '선택된 관심사가 없습니다.'
        })
    
    tag_ids = list(map(int, tag_ids))
    tags = InterestTag.objects.filter(tag_id__in=tag_ids)
    jobs_raw = Job.objects.filter(related_tags__tag_id__in=tag_ids).distinct()

    # keyword_tags를 쉼표로 split해서 넘겨줌
    jobs = []
    for job in jobs_raw:
        job.keyword_tags_list = [tag.strip() for tag in job.keyword_tags.split(',')] if job.keyword_tags else []
        jobs.append(job)

    return render(request, 'match/m_job.html', {
        'tags': tags,
        'jobs': jobs,
        'message': None if jobs else '이 관심사에 해당하는 직무가 없습니다.'
    })

# http://127.0.0.1:8000/match/job_detail/ 의 view (선택한 직무 상세보기)
#@login_required
#def job_detail_view(request):
#    job_id = request.GET.get('job_id')
#    job = get_object_or_404(Job, job_id=job_id)
#    return render(request, 'match/m_job_detail.html', {'job': job})

