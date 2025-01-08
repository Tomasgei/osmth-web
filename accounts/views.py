from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.http import JsonResponse
from .models import Profile
from documents.models import SharedDocument
from events.models import Event
from .forms import ProfileForm
from django.shortcuts import render
from django.contrib import messages

#MeetingRecord, Event, Project

@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == 'POST':  # Zpracování dat z modalu
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil byl úspěšně aktualizován.')  # Zpráva o úspěchu
            return JsonResponse({'success': True})  # AJAX odpověď
        else:
            return JsonResponse({'success': False, 'errors': form.errors})  # Chyby z validace formuláře

    form = ProfileForm(instance=profile)
    shared_documents = SharedDocument.objects.all().order_by('-uploaded_at')  # Seřadit podle data přidání
    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'form': form,
        'shared_documents': shared_documents
    })


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
