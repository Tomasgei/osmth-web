from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django_resized import ResizedImageField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('regular', 'Běžný uživatel'),
        ('commander', 'Komtur'),
        ('k9', 'K9'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='regular')

    # Přidání related_name k polím groups a user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def is_commander(self):
        return self.role == 'commander'

    def is_k9(self):
        return self.role == 'k9'



class Profile(models.Model):
    RANK_CHOICES = [
        ('friend', 'Přítel řádu'),
        ('squire', 'Zbrojnoš'),
        ('knight', 'Rytíř'),
        ('dame', 'Dáma'),
    ]
    GENDER_CHOICES = [
        ('male', 'Muž'),
        ('female', 'Žena'),
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commandery = models.ForeignKey(
        'structure.Commandery',  # Lazy reference
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    rank = models.CharField(max_length=50, choices=RANK_CHOICES, default='friend')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    photo = ResizedImageField(force_format='WEBP', quality=75, null=True, blank=True, upload_to="avatars/")
    first_name = models.CharField(max_length=100, blank=True, verbose_name="Jméno")
    last_name = models.CharField(max_length=100, blank=True, verbose_name="Příjmení")
    registration_date = models.DateField(auto_now_add=True, verbose_name="Datum registrace")
    commandery = models.ForeignKey('structure.Commandery', on_delete=models.SET_NULL, null=True, blank=True, related_name='profile_members', verbose_name="Příslušná komenda")
    area = models.ForeignKey('structure.Area', on_delete=models.SET_NULL, null=True, blank=True, related_name='members', verbose_name="Příslušná oblast")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def clean(self):
        if self.rank == 'dame' and self.gender != 'female':
            raise ValidationError("Pouze ženy mohou být Dámy.")
        if self.rank == 'knight' and self.gender == 'female':
            raise ValidationError("Ženy s rolí Rytíř musí být označeny jako Dáma.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.get_rank_display()}"
