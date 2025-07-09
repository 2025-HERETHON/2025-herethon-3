from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
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
        
def login_view(request):
    # GET 요청 시 로그인 폼 응답
    if request.method == 'GET':
        return render(request, 'users/login.html', {'form': AuthenticationForm()})
    else:
        # POST 요청 시 로그인 처리
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:home')
            else:
                return render(request, 'users/login.html', {'form': form, 'error': '유효하지 않은 정보입니다.'})
        else:
            return render(request, 'users/login.html', {'form': form, 'error': '유효하지 않은 정보입니다'})
        

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
    # 로그아웃 처리
    logout(request)
    return redirect('users:home')

def home(request):
    return render(request, 'users/home.html')
