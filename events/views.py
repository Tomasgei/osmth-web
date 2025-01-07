from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Event, EventParticipation
from .forms import EventForm

@login_required
def event_list(request):
    events = Event.objects.filter(status='planned').order_by('date_time')

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'events/event_list.html', {'events': events, 'form': form})

@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    participants = event.participants.all()
    user_participation = participants.filter(user=request.user).exists()

    if request.method == 'POST' and 'join_event' in request.POST:
        if not user_participation:
            EventParticipation.objects.create(event=event, user=request.user)
        return redirect('event_detail', event_id=event.id)

    if request.method == 'POST' and 'leave_event' in request.POST:
        if user_participation:
            participants.filter(user=request.user).delete()
        return redirect('event_detail', event_id=event.id)

    return render(request, 'events/event_detail.html', {
        'event': event,
        'participants': participants,
        'user_participation': user_participation,
    })
