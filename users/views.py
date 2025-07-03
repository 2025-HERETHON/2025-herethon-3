from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout 
# Create your views here.

def signup_view(request):
    # GET 요청 시 회원가입 폼 응답
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})
    
    # POST 요청 시 데이터 확인 후 회원가입 처리
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 로그인 처리
            login(request, user)
            return redirect('users:home')
        else:
            # 폼이 유효하지 않은 경우 에러 메시지와 함께 폼 재렌더링
            return render(request, 'users/signup.html', {'form': form})
        
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

def logout_view(request):
    # 로그아웃 처리
    logout(request)
    return redirect('users:home')

def home(request):
    return render(request, 'users/home.html')
