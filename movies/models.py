from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    director = models.CharField(max_length=100)
    actors = models.TextField(max_length=200)
    release_date = models.DateField()
    thumb = models.ImageField(default='default.jpg',blank=True)
    author = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.movie.title}'