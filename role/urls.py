from django.urls import path
from .views import job_roles_view

app_name = 'role'

urlpatterns = [
    path('job/<int:job_id>/roles/', job_roles_view, name='job_roles'),
]
