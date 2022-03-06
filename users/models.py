from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from time import timezone
from django.utils import timezone
from design.models import Post



# Create your models here.



class UserPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name = 'userlike')

    def total_likes(self):
        return (f'{self.likes.count()} Likes')
        
    def __str__(self):
        return self.contents



class UsersRequest(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=60)
    brand = models.ForeignKey(Post, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return (f'{self.author} ---> {self.brand}')
    


class UserComment(models.Model):
    author = models.CharField(max_length= 100)
    post = models.ForeignKey(UserPost,on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    time = models.TimeField(verbose_name='Time', auto_now_add=True)

    def __str__(self):
        return (f'{self.comment} ... {self.time}')
        