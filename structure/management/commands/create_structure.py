from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from structure.models import Area, Commandery, Membership
import random

class Command(BaseCommand):
    help = "Vytvoření testovací struktury pro aplikaci"

    def handle(self, *args, **options):
        # Pomocná funkce pro vytvoření nebo získání uživatele
        def create_or_get_user(username, email, password):
            user, created = User.objects.get_or_create(username=username, defaults={'email': email})
            if created:
                user.set_password(password)
                user.save()
            return user

        # Pomocná funkce pro vytvoření nebo získání profilu
        def create_or_get_profile(user, **kwargs):
            profile, created = Profile.objects.get_or_create(user=user, defaults=kwargs)
            return profile

        # Vytvoření uživatelů K9
        k9_usernames = ['k9_user1', 'k9_user2']
        k9_users = []
        for username in k9_usernames:
            user = create_or_get_user(username, f"{username}@templar.org", "password123")
            create_or_get_profile(
                user=user,
                rank='knight',
                first_name=username.capitalize(),
                last_name="Admin"
            )
            k9_users.append(user)

        # Vytvoření oblastí
        areas = []
        for i in range(1, 4):
            area = Area.objects.create(
                name=f"Oblast {i}",
                description=f"Popis oblasti {i}"
            )
            areas.append(area)

        # Vytvoření komturů
        komtur_users = []
        for i in range(1, 4):
            user = create_or_get_user(f"komturo_user{i}", f"komturo_user{i}@templar.org", "password123")
            create_or_get_profile(
                user=user,
                rank='knight',
                first_name=f"Komtur{i}",
                last_name="Leader"
            )
            komtur_users.append(user)

        # Vytvoření komend
        comms = []
        for i, area in enumerate(areas):
            comm = Commandery.objects.create(
                name=f"Komenda {i+1}",
                description=f"Popis komendy {i+1}",
                area=area,
                komtur=komtur_users[i]
            )
            comms.append(comm)

        # Vytvoření členů
        ranks = ['friend', 'squire', 'knight', 'dame']
        for i, commandery in enumerate(comms):
            for j in range(1, 11):
                user = create_or_get_user(f"member_{i+1}_{j}", f"member_{i+1}_{j}@templar.org", "password123")
                create_or_get_profile(
                    user=user,
                    rank=random.choice(ranks),
                    first_name=f"Member{i+1}{j}",
                    last_name="Templar",
                    commandery=commandery,
                    area=commandery.area
                )

        self.stdout.write(self.style.SUCCESS("Testovací struktura byla úspěšně vytvořena."))
