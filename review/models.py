from django.db import models



class Review(models.Model):
    username = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    STAR_CHOICES= [
    ('★', '★'),
    ('★★', '★★'),
    ('★★★', '★★★'),
    ('★★★★', '★★★★'),
    ('★★★★★', '★★★★★'),
    ]

    star = models.CharField(max_length=5, choices=STAR_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





