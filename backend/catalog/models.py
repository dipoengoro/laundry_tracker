from django.conf import settings
from django.db import models

class ClothingItem(models.Model):
    CATEGORY_CHOICES = [
        ('TOP', 'Atasan'),
        ('BOTTOM', 'Bawahan'),
        ('OUTWEAR', 'Luaran'),
        ('OTHER', 'Lainnya'),
    ]

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='clothing_items')
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='TOP')
    color = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='clothing_images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) milik {self.owner.username}"
