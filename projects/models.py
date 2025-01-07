from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    objectives = models.TextField(blank=True, null=True)
    skills_needed = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('idea', 'Nápad'), ('ready', 'Připraveno'), ('in_progress', 'Probíhá')],
        default='idea'
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)  # Přidáno pole pro obrázek

    def __str__(self):
        return self.name


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments', verbose_name="Projekt")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Uživatel")
    content = models.TextField(verbose_name="Komentář")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vytvořeno")

    def __str__(self):
        return f"Komentář od {self.user.username}"


class Interest(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='interests', verbose_name="Projekt")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Uživatel")

    def __str__(self):
        return f"{self.user.username} má zájem o projekt {self.project.name}"
