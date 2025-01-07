from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.http import JsonResponse
from .models import Profile
from documents.models import SharedDocument
from events.models import Event
from .forms import ProfileForm
from django.shortcuts import render

#MeetingRecord, Event, Project

@login_required
def profile_view(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    shared_documents = SharedDocument.objects.all().order_by('-uploaded_at')  # Seřadit podle data přidání
    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'form': form,
        'shared_documents': shared_documents
    })

@login_required
def profile_edit(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  # request.FILES je klíčové
        if form.is_valid():
            form.save()
            return redirect('profile')  # Přesměrování na profil
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html', {'form': form})



@login_required
def dashboard_view(request):
    shared_documents = SharedDocument.objects.all()
    #meeting_records = MeetingRecord.objects.all()
    events = Event.objects.all()
    #ongoing_projects = Project.objects.filter(status='in_progress')
    return render(request, 'accounts/dashboard.html', {
        'shared_documents': shared_documents,
        #'meeting_records': meeting_records,
        'events': events,
        #'ongoing_projects': ongoing_projects,
    })
