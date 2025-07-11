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
        selected_tag_ids = request.POST.getlist('tag_ids') 
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
    
    return render(request, 'match/interest_selection_intro.html', {'tags': tags})

# http://127.0.0.1:8000/match/job/ 화면 view
@login_required
def job_select_view(request):
    if request.method == 'POST':
        selected_tag_names = request.POST.get('interests', '').split(',')
        selected_tag_names = [name.strip() for name in selected_tag_names if name.strip()]
        print("🔍 선택된 관심사:", selected_tag_names)

        # 기존 선택 삭제
        UserSelectedTag.objects.filter(user=request.user).delete()

        # 관심사 이름으로 태그 저장
        selected_tags = []
        for tag_name in selected_tag_names:
            try:
                tag = InterestTag.objects.get(tag_name=tag_name)
                UserSelectedTag.objects.create(user=request.user, tag=tag)
                selected_tags.append(tag)
            except InterestTag.DoesNotExist:
                print(f"관심사 '{tag_name}' 존재하지 않음")

        # 관심사에 따른 직무 추천 (3개 제한)
        recommended_jobs = Job.objects.filter(related_tags__in=selected_tags).distinct()[:3]

        # interests는 템플릿에서 JS로 넘기기 위한 리스트 (string list)
        interests = ['#' + tag.tag_name for tag in selected_tags]

        return render(request, 'jobs/job_recommendation_tab.html', {
            'interests': interests,
            'jobs': recommended_jobs
        })

    # GET 요청 시 관심사 선택 페이지 렌더
    return render(request, 'match/interest_selection_tab.html')

# http://127.0.0.1:8000/match/job_detail/ 의 view (선택한 직무 상세보기)
#@login_required
#def job_detail_view(request):
#    job_id = request.GET.get('job_id')
#    job = get_object_or_404(Job, job_id=job_id)
#    return render(request, 'match/m_job_detail.html', {'job': job})

@login_required
def interest_selection_view(request):
    return render(request, 'match/interest_selection_tab.html')
