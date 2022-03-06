from audioop import reverse
from pdb import post_mortem
from sre_constants import SUCCESS
from sys import hash_info
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                CreateView,
                                DetailView,
                                UpdateView,
                                DeleteView,
                                TemplateView
                                )
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from design.templates.design.forms import PosteCreateForm
from .models import Order, OrderItem, Post,Lady,Children,Car,Shoe,Handbag,Phone
from users.models import UserPost
#from django.utils import reverse
from PIL import Image
from django.db import models
from django.http import HttpResponseRedirect
from django.contrib import messages
import json

# Create your views here.
def Home(request):
     posts = Post.objects.all()
     cars = Car.objects.all()
     phones = Phone.objects.all()
     shoes = Shoe.objects.all()
     #ordering = ['-date']

     handbags = Handbag.objects.all()
     return render(request,'design/home.html',{'phone':phones, 'post': posts, 'cars':cars, 'handbags':handbags, 'shoe':shoes,})
    

class CarsView(ListView):
    model = Car
    context_object_name = 'cars'
    

class ShoesView(ListView):
    model = Shoe
    context_object_name = 'shoes'

class HandbagView(ListView):
    model = Handbag
    context_object_name = 'handbags'

class PhoneView(ListView):
    model = Phone
    context_object_name = 'phones'

def HomeListView(request):
    model = Post
#     template_name = 'design/home.html'
#     #context_object_name = ('Posts','Ladys')
   # ordering = ['-date']  
def updateItems(request):
     data =json.loads(request.body)
     productId = data['productId']
     action = data['action']
     print('productId',productId)
     print('Action:',action)
     author = request.user
     print(author)
     product = Car.objects.get(id=productId)
     print(product)
     order,created = Order.objects.get_or_create(author=author)
     orderItem,created = OrderItem.objects.get_or_create(order=order, product = product)
     if action =='add':
         orderItem.quantity = (orderItem.quantity + 1)
     elif action =='remove':
         orderItem.quantity = (orderItem.quantity - 1)
     orderItem.save()
     if orderItem.quantity <=0:
         orderItem.delete()
     return JsonResponse('Items Added to cart', safe=False)


class PostDetails(DetailView):
    model =  Post

class LadiesDetailView(DetailView):
    model = Lady
class ChildrenDetailView(DetailView):
    model = Children


class PostUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    #image = models.ImageField(default = 'user.jpg', upload_to = 'Design_Images')
    fields = ['image', 'title','cost', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
            post =self.get_object()
            if self.request.user == post.author:
                return True
            return False

class UserPostUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = UserPost
    fields = ['contents']
    template_name = 'design/post_form.html'
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
            post =self.get_object()
            if self.request.user == post.author:
                return True
            return False

    # @property
    # def get_image_url(self):
    #     if self.image and hasattr(self.image, 'url'):
    #         return self.image.url
    #     else:
    #         return "/static/images/user.jpg"

    
class PostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

#user delete class view
class UserPostDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = UserPost
    success_url = '/blog'
    template_name = 'design/userpost_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


# class UserCommentsView(CreateView):
#     model = Comment
#     template_name = 'users/usersrequest_form.html'
#     success_url = '/details/object.id'
#     fields = ['coment']
#     def form_valid(self, form):
#         form.instance.post = self.request.objects.id
#         #form.instance.author = self.request.user
#         obj = form.save(commit=False)
#         obj.author = self.request.user
#         obj.save
#         return super().form_valid(form)

class CreatePostView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Post
    fields = ['image','title', 'content','cost']
    success_url = '/'
    
    def form_valid(self, form):
        #form.instance.author = self.request.user
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save
        return super().form_valid(form)

    def test_func(self):
        #post = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False 


    # def form_invalid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_invalid(form)

class CreateLadyView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Lady
    fields = ['image','title', 'Descriptions','cost']
    success_url = '/'
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class CreateChildrenView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Children
    fields = ['image','title', 'Descriptions','cost']
    success_url = '/'
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class CreatePhoneView(LoginRequiredMixin,CreateView):
    model = Phone
    fields = ['image','title', 'Descriptions','cost']
    success_url = '/'
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

#car form view
class CreateCarView(LoginRequiredMixin,CreateView):
    model = Car
    fields = ['image','title', 'Descriptions','cost']
    success_url = '/'
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

# handbag creation view
class CreateHandBagView(LoginRequiredMixin,CreateView):
    model = Handbag
    fields = ['image','title', 'Descriptions','cost']
    success_url = '/'
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

#Creating the Shoe posting view
class CreateShoeView(LoginRequiredMixin,CreateView):
    model = Shoe
    fields = ['image','title', 'Descriptions','cost']
    success_url = '/'
    def form_valid(self,form):
        obj = form.save(commit = False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)

def about(request):
    return render(request, 'design/about.html', {'title':'We Sell Allm Kinds'})


def Login(request):
    messages.success(request, 'Login Was Succesful')
    #<script src="{% static 'design/assets/js/script.js' %}" type="text/javascript"></script>  
    return render(request, 'design/')

