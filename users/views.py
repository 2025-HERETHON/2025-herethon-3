from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from jobs.models import UserLikedJob
from jobs.models import Job
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponse(f"회원가입 성공! 생성된 유저: {user.user_id}")
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



def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': LoginForm()})
    else:
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('username')  # ← 여기 반드시 'username'
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_id, password=password)  # 'username' 파라미터로 전달
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'users/login.html', {'form': form, 'error': '유효하지 않은 정보입니다.'})
        else:
            return render(request, 'users/login.html', {'form': form, 'error': '유효하지 않은 정보입니다.'})



def logout_view(request):
    
    # 로그아웃 처리
    logout(request)
    return redirect('home')


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
   
    recent_ids = request.session.get('recent_jobs', [])
    recent_jobs = Job.objects.filter(job_id__in=recent_ids)
    return render(request, 'users/home.html', {
        'username': request.user.username,
        'recent_jobs': recent_jobs
    })


def mypage_view(request):
    liked_jobs = UserLikedJob.objects.filter(user=request.user).select_related('job')[:3]  # 최대 3개
    # 세션에 저장된 최근 본 직무 리스트 가져오기
    return render(request, 'users/mypage.html', {
        'liked_jobs': liked_jobs,       
        'username': request.user.username,
    })

