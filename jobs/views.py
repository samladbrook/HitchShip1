# jobs/views.py

from django.shortcuts import get_object_or_404, redirect, render
from .models import Job
from .forms import JobForm

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Or wherever you want to redirect after saving
    else:
        form = JobForm(user=request.user)
    
    return render(request, 'jobs/add_job.html', {'form': form})

def home(request):
    if request.user.is_authenticated:
        jobs_added_by_user = Job.objects.filter(added_by=request.user)
        print(f"Current User: {request.user}")
        print(f"Jobs Added by User: {jobs_added_by_user}")
        return render(request, 'home.html', {
            'jobs': jobs_added_by_user,
        })
    else:
        return render(request, 'home.html', {
            'jobs': [],
        })
    

def delete_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login if user is not authenticated
    
    job = get_object_or_404(Job, id=job_id, added_by=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('home')  # Redirect to home page after deletion
    return redirect('home') 

def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, added_by=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = JobForm(instance=job)

    return render(request, 'jobs/add_job.html', {'form': form})