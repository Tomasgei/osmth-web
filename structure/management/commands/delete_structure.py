from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from structure.models import Area, Commandery, Membership

class Command(BaseCommand):
    help = "Smazání testovací struktury z databáze"

    def handle(self, *args, **options):
        # Smazání členství
        Membership.objects.all().delete()

        # Smazání komend
        Commandery.objects.all().delete()

        # Smazání oblastí
        Area.objects.all().delete()

        # Smazání profilů a uživatelů
        profile_users = Profile.objects.filter(
            user__username__startswith=('k9_user', 'komtur_user', 'member_')
        )
        for profile in profile_users:
            profile.user.delete()

        self.stdout.write(self.style.SUCCESS("Testovací struktura byla úspěšně smazána."))
