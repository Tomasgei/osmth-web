from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Area(models.Model):
    name = models.CharField(max_length=255, verbose_name="Název oblasti")
    description = models.TextField(blank=True, null=True, verbose_name="Popis oblasti")

    def __str__(self):
        return self.name

class Commandery(models.Model):
    name = models.CharField(max_length=255, verbose_name="Název komendy")
    description = models.TextField(blank=True, null=True, verbose_name="Popis komendy")
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="commanderies", verbose_name="Příslušná oblast")
    komtur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    @property
    def member_count(self):
        return self.members.count()

class Membership(models.Model):
    commandery = models.ForeignKey(Commandery, on_delete=models.CASCADE, related_name="membership_members", verbose_name="Komenda")
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="membership", verbose_name="Člen")
    joined_at = models.DateField(auto_now_add=True, verbose_name="Datum připojení")

    def __str__(self):
        return f"{self.user.username} - {self.commandery.name}"
