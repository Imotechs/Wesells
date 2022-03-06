from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from design.models import Post,Comment
from time import timezone
from email.policy import default
import re
from django import forms
from django.utils import timezone
from django.db import models

class PosteCreateForm(UserCreationForm):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Design_Images')
    author = models.ForeignKey(User, on_delete=models. CASCADE)
    title = models.CharField(max_length= 50)
    cost = models.CharField(max_length=10, default='NGN 0.00')
    date = models.DateTimeField(default = timezone.now)
    class Meta:
        model = Post
        fields = ['author','title','image','cost']

    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width >300:
    #         imageparam = (300, 300)
    #         img.thumbnail(imageparam)
    #         img.save(self.image.path)

