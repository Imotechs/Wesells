from asyncio import exceptions
from gc import get_objects
from pyexpat.errors import messages
from urllib import request
from urllib.parse import uses_relative
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView
from users.forms import (
    UserRegisterForm,
    UserCommentForm
)
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.auth.models import User
from design.models import Post
from .models import UserPost, UsersRequest, UserComment
from django.contrib import messages
# Create your views here.

from reportlab.pdfgen import canvas
from django.http import FileResponse
import io


def pdfview(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    username = request.user 
    p.drawString(10,10, f'Hello {username}')
    #p.drawString('Adzembeh Joshua')

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer,as_attachment=True,filename='files.pdf')


def Register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username','email')
            messages.success(request, f' Account for {username} was created!  Login Now')
            return redirect('login')  
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'title':'Registration','form':form })


class BlogPostViw(LoginRequiredMixin, ListView):
    model = UserPost
    template_name = 'my_blog/userpost_list.html'
    context_object_name = 'userposts'
    ordering = ['-date']
    #paginate_by = 3


class PlaceOdderFormView(CreateView):
    model = UsersRequest
    fields = ['address', 'brand', 'quantity']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/'

class DashbaordView(UserPassesTestMixin,ListView):
    model = UsersRequest
    context_object_name = 'usersrequests'
    template_name = 'users/usersrequest_list.html'
    ordering = ['-date']
    
    
    def test_func(self):
        #post = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False 



class Homeplaceorder(LoginRequiredMixin, CreateView):
    model =UsersRequest
    fields = ['address', 'brand','quantity']
    template_name = 'users/usersrequest_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/'

class UserCreatePostView(LoginRequiredMixin, CreateView):
    model = UserPost
    fields = ['contents']
    template_name = 'users/usersrequest_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    success_url = '/blog/'

@login_required
def LikePost(request,pk):

        post = get_object_or_404(Post, id= request.POST.get('post_id'))
        post.likes.add(request.user)
        return HttpResponseRedirect(reverse('design:details', args=[str(pk)]))
    

def UserLikePost(request,pk):
    Post = get_object_or_404(UserPost, id= request.POST.get('userpost_id'))
    Post.likes.add(request.user)
    return HttpResponseRedirect(reverse('design:blog'))

def UserCommentPostView(request, pk):
    if request.method == 'POST':
        form = UserCommentForm(request.POST)
        post = get_object_or_404(UserPost,id = request.POST.get('usercomment_id'))

        if form.is_valid():
            UserComment.add(post, form.comment)
            return HttpResponseRedirect(reverse('design:blog', args =[str(pk)]))
            # form.save()
            # comment = form.cleaned_data.get('comment')
            # messages.success(request, f' comment was created for the Post')
            # return redirect('/blog')
    else:
        form = UserCommentForm()
        return render(request, 'users/comment_form.html', {'form':form})


    
    # UserComment.add(request.form)
    # return HttpResponseRedirect(reverse('design:blog', args =[str(pk)]))
