from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, null=True)
    website_url = models.CharField(max_length=50, blank=True, null=True)
    tg_url = models.CharField(max_length=50, blank=True, null=True)
    fb_url = models.CharField(max_length=50, blank=True, null=True)
    insta_url = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    header_image = models.ImageField(upload_to='images/', blank=True, null=True)
    title_tag = models.CharField(max_length=100, blank=True, default='Behzod')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = RichTextField(blank = True, null = True)
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='general')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('home')