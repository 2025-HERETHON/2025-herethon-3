# jobs/urls.py

from django.urls import path
from .views import *

app_name = 'jobs'

urlpatterns = [
     #path('test/', test_job_list, name='test_job_list'),  # 테스트용 URL
     path('<str:job_id>/', job_detail, name='job_detail'),  # 상세 보기 연결
     path('<int:job_id>/like/', like_job_view, name='like_job'), # 하트 누르기 연결
   
]
