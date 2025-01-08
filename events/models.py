from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Event(models.Model):
    STATUS_CHOICES = [
        ('planned', 'Plánovaná'),
        ('ongoing', 'Probíhá'),
        ('completed', 'Dokončená'),
    ]

    name = models.CharField(max_length=255, verbose_name="Název akce")
    location = models.CharField(max_length=255, verbose_name="Místo konání")
    date_time = models.DateTimeField(verbose_name="Čas konání")
    description = models.TextField(verbose_name="Popis")
    image = models.ImageField(upload_to='event_images/', blank=True, null=True, verbose_name="Ilustrační obrázek")
    capacity = models.PositiveIntegerField(default=0, verbose_name="Maximální kapacita")
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="Organizátor")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planned', verbose_name="Stav")
    open_until = models.DateTimeField(blank=True, null=True, verbose_name="Přihlášení otevřeno do")
    notes = models.TextField(blank=True, null=True, verbose_name="Dodatečné poznámky")

    def __str__(self):
        return self.name

class EventParticipation(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='participations')
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name="Datum potvrzení účasti")

    def __str__(self):
        return f"{self.user.username} účast na {self.event.name}"
