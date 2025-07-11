from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from jobs.models import UserLikedJob
from jobs.models import Job
from match.models import UserSelectedTag
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request,'match/interest_selection_intro.html')
        else:
            print("❌ 폼 에러:", form.errors)
            return render(request, 'users/signup.html', {
                'form': form,
                'user_id': request.POST.get('user_id'),
                'name': request.POST.get('name'),
                'email': request.POST.get('email'),
            })
    else:
        form = SignUpForm()
        return render(request, 'users/signup.html', {
            'form': form
        })

# 아이디 중복 체크
@csrf_exempt
def check_user_id_view(request):
    print("🔥 요청 도달:", request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_id = data.get('user_id', '').strip()

            exists = get_user_model().objects.filter(user_id=user_id).exists()

            return JsonResponse({
                'exists': exists,
                'message': '이미 사용 중인 아이디입니다.' if exists else '사용 가능한 아이디입니다!'
            })
        except Exception as e:
            print("🚨 서버 에러:", e)
            return JsonResponse({'error': '서버 처리 중 오류 발생'}, status=500)
    return JsonResponse({'error': '허용되지 않은 메서드입니다.'}, status=405)



@csrf_exempt  # CSRF 토큰을 우회하려면 이 데코레이터가 필요합니다. (그러나 배포 환경에서는 CSRF를 비활성화하지 마세요)
def login_view(request):
    if request.method == "GET":
        return render(request, 'users/login.html')  # 로그인 폼 렌더링

    elif request.method == "POST":
        data = json.loads(request.body)  # POST 데이터 읽기
        user_id = data.get('user_id')
        password = data.get('password')

        user = authenticate(request, user_id=user_id, password=password)

        if user is not None:
            login(request, user)  # 로그인 성공
            return JsonResponse({'success': True})  # 성공한 경우 JSON 응답
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)


@csrf_exempt
def check_user_id_view(request):
    print("🔥 요청 도달:", request.method)
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_id = data.get('user_id', '').strip()

            exists = get_user_model().objects.filter(user_id=user_id).exists()

            return JsonResponse({
                'exists': exists,
                'message': '이미 사용 중인 아이디입니다.' if exists else '사용 가능한 아이디입니다!'
            })
        except Exception as e:
            print("🚨 서버 에러:", e)
            return JsonResponse({'error': '서버 처리 중 오류 발생'}, status=500)
    return JsonResponse({'error': '허용되지 않은 메서드입니다.'}, status=405)

def logout_view(request):
    print("✅ logout_view 진입함")  # 서버 콘솔에 출력 확인
    logout(request)
    return redirect('onboarding')

def onboarding_view(request):
    return render(request, 'users/onboarding.html')

# 아이디 찾기
def find_user_id_view(request):
    User = get_user_model()
    user_id_result = None

    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            user_id_result = f"아이디는 '{user.user_id}' 입니다."
        except User.DoesNotExist:
            user_id_result = "해당 이메일로 가입된 사용자가 없습니다."

    return render(request, 'users/find_user_id.html', {'user_id_result': user_id_result})



@login_required
def home_view(request):
    # 사용자가 선택한 관심사
    interest_tags = (
    UserSelectedTag.objects.filter(user=request.user)
    .select_related('tag')  # ForeignKey 최적화
    .values_list('tag__tag_name', flat=True)
    .distinct()
)


    # 최근 본 직무
    recent_ids = request.session.get('recent_jobs', [])
    recent_jobs = Job.objects.filter(job_id__in=recent_ids)[:3]

    return render(request, 'users/home.html', {
        'username': request.user.username,
        'recent_jobs': recent_jobs,
        'recent_interests': list(interest_tags),  # ✅ 리스트 그대로 넘김
    })


def mypage_view(request):
    liked_jobs = UserLikedJob.objects.filter(user=request.user).select_related('job')[:4]  # 최대 3개
    
    return render(request, 'users/mypage.html', {
        'liked_jobs': liked_jobs,       
        'username': request.user.username,
    })

