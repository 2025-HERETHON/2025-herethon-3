from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

# users/urls.py



urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('signup/check_user_id/', check_user_id_view, name='check_user_id'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('find_user_id/',find_user_id_view, name='find_user_id'),
    # 비밀번호 재설정 요청 (이메일 입력)
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registrations/password_reset.html',
        email_template_name='registrations/password_reset_email.html',
        success_url='/password_reset_done/',
    ), name='password_reset'),

    # 이메일 발송 완료 안내
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registrations/password_reset_done.html'
    ), name='password_reset_done'),

    # 메일의 링크 클릭 → 비번 재설정 폼
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registrations/password_reset_confirm.html',
        success_url='/reset_done/',
    ), name='password_reset_confirm'),

    # 비밀번호 변경 완료
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(
        
        template_name='registrations/password_reset_complete.html'
    ), name='password_reset_complete'),
]
