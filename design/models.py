#from typing_extensions import Self
from urllib import request
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.db import models
from django.forms import CharField, ImageField, forms
from django.contrib.auth.models import User
from time import timezone
from django.utils import timezone
from PIL import Image


# Create your models here.

     #user_detail = CustomUser.objects.filter(id = id)
class Phone(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Ladies/Design_Images' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)
    Descriptions = models.TextField()
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)
    def __str__(self):
        return self.title[self.date]
    

class Post(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Design_Images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length= 50)
    cost = models.IntegerField()
    date = models.DateTimeField(default = timezone.now)
    likes = models.ManyToManyField(User, related_name='like')
    content = models.TextField( default = ' The Fashion that suit your reputation',max_length= 500)
    #dislikes = models.IntegerField(default=0)
    #url= models.SlugField(max_length=300, default = f'{title}-{author}-{cost}-{date}')
     
    # @property
    # def get_image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return "/static/images/user.jpg"
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        # all_likes = get_object_or_404(Post, id = self.kwargs['pk'])
        # total_likes = all_likes.total_likes()
        # count = 
        return self.title

    def get_absolute_url(self):
        return reverse('design:details', kwargs = {"pk":self.pk})

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            imageparam = (400, 400)
            img.thumbnail(imageparam)
            img.save(self.image.path)
    
    # def save(self, *args, **kwargs):
    #     self.url= slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)
   

class Comment(models.Model):
     post = models.ForeignKey(Post, related_name = 'coments',on_delete=models.CASCADE)
     coment =models.TextField()
     date = models.DateTimeField(auto_now=True)
     username = models.CharField(max_length=50, default= 'admin')
     def __str__(self):
         return (f'{self.post.title} ---> {self.username}')

    #  def get_absolute_url(self):
    #     return reverse('design:details', kwargs = {"pk":self.pk})
class Car(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Cars/Design_Images' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    Descriptions = models.TextField()
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)

class Order(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    #item = models.ForeignKey(Car,on_delete=models.SET_NULL,)
    transaction_id = models.SlugField(max_length=20, null=True)
    def __str__(self):
        return self.item[self.id]

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 


class OrderItem(models.Model):
	product = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class Shoe(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Shoes/Design_Images' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    Descriptions = models.TextField()
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)
   
class Handbag(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Handbarg/Design_Images' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    Descriptions = models.TextField()
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)

class Lady(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to = 'Ladies/Design_Images' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    Descriptions = models.TextField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('design:ladydetails', kwargs = {"pk":self.pk})
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            imageparam = (300, 300)
            img.thumbnail(imageparam)
            img.save(self.image.path)

class Children(models.Model):
    #post_id = models.AutoField(primary_key=True)
    image = models.ImageField(default = 'default.jpg', upload_to = 'Children/Design_Images' )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    cost = models.IntegerField()
    Descriptions = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Design:details', kwargs={"pk":self.pk})
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width > 300:
            imgparam = (300,300)
            img.thumbnail(imgparam)
            img.save(self.image.path)
