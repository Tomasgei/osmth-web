from django.db import models

class SharedDocument(models.Model):
    DOCUMENT_TYPE_CHOICES = [
        ('general', 'Obecné'),
        ('meeting', 'Zápisy z jednání'),
    ]
    name = models.CharField(max_length=255, verbose_name="Název dokumentu")
    file = models.FileField(upload_to='shared_documents/', verbose_name="Soubor")
    document_type = models.CharField(
        max_length=10,
        choices=DOCUMENT_TYPE_CHOICES,
        default='general',
        verbose_name="Typ dokumentu"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Nahráno dne")

    def __str__(self):
        return f"{self.name} ({self.get_document_type_display()})"
