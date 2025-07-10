from django.shortcuts import render, get_object_or_404
from jobs.models import Job
from role.models import Role

def job_roles_view(request, job_id):
    job = get_object_or_404(Job, job_id=job_id)
    roles = Role.objects.filter(job=job)

    return render(request, 'role/role.html', {
        'roles': roles,
        'job': job
    })
