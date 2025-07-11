from django.urls import path
from .views import *

app_name='match'

urlpatterns = [
    path('', match_home, name='match_home'),
    path('choose/', choose_interest_view, name='m_choose'),
    path('job/', job_select_view, name='m_job_select'),
    path('interests/', interest_selection_view, name='interests'),
    #path('job_detail/', job_detail_view, name='m_job_detail'),
]