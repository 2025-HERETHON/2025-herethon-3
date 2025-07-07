from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('find_user_id/',find_user_id_view, name='find_user_id'),
]