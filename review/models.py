from django.db import models


STAR_CHOICES= [
    ('★', '★'),
    ('★★', '★★'),
    ('★★★', '★★★'),
    ('★★★★', '★★★★'),
    ('★★★★★', '★★★★★'),
    ]
class Review(models.Model):
    username = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    star = models.CharField(max_length=6, choices=STAR_CHOICES, default='★')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





