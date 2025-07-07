from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
# Create your views here.

def signup_view(request):
    User = get_user_model()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        name_checked = request.POST.get('name_checked')

        # (1) 아이디 중복 확인 버튼 클릭 시
        if 'check_name' in request.POST:
            if User.objects.filter(user_id=user_id).exists():
                return render(request, 'users/signup.html', {
                    'form': form,
                    'name_error': '이미 사용 중인 아이디입니다.',
                    'name_checked': 'false',
                    'user_id': user_id,
                    'name': name,
                    'email': email,
                })
            else:
                return render(request, 'users/signup.html', {
                    'form': form,
                    'name_error': '사용 가능한 아이디입니다!',
                    'name_checked': 'true',
                    'user_id': user_id,
                    'name': name,
                    'email': email,
                })

        # (2) 중복 확인 안했을 때
        if name_checked != 'true':
            return render(request, 'users/signup.html', {
                'form': form,
                'name_error': '아이디 중복 확인을 먼저 해주세요.',
                'name_checked': 'false',
                'user_id': user_id,
                'name': name,
                'email': email,
            })

        # (3) 회원가입 진행
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            # 회원가입 실패 시 form 에러 출력
            print(form.errors)  # 🔹 서버 로그에서 확인 가능
            return render(request, 'users/signup.html', {
                'form': form,
                'name_checked': 'true',
                'user_id': user_id,
                'name': name,
                'email': email,})

           

    else:
        
        form = SignUpForm()
        return render(request, 'users/signup.html', {
            'form': form,
            'name_checked': 'false',
        })



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


def home(request):
    return render(request, 'users/home.html')
