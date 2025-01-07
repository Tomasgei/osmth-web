from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django_resized import ResizedImageField

class Profile(models.Model):
    ROLE_CHOICES = [
        ('knight', 'Rytíř'),
        ('dame', 'Dáma'),
        ('squire', 'Zbrojnoš'),
        ('commander', 'Komtur'),
    ]
    GENDER_CHOICES = [
        ('male', 'Muž'),
        ('female', 'Žena'),

    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = ResizedImageField(force_format='WEBP',quality=75,null=True, blank=True, upload_to="avatars/")

    def clean(self):
        if self.role == 'dame' and self.gender != 'female':
            raise ValidationError("Pouze ženy mohou být Dámy.")
        if self.role == 'knight' and self.gender == 'female':
            raise ValidationError("Ženy s rolí Rytíř musí být označeny jako Dáma.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
