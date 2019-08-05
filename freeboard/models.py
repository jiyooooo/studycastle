from django.db import models


class Freeboard(models.Model):
    username = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FreeboardLikepoint(models.Model):
    freeboard = models.ForeignKey(Freeboard, on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    like_point = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    freeboard = models.ForeignKey(Freeboard, on_delete=models.CASCADE)
    username = models.CharField(max_length=10)
    content = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)