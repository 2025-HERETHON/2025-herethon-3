from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('check_user_id/', check_user_id_view, name='check_user_id'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]