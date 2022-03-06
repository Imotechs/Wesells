"""OBCLASSICS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,reverse_lazy
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'users'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('design.urls')),
    path('register/', user_views.Register, name= 'register'),
    path('profilePdf/', user_views.pdfview, name = 'pdfgen'),
    path('like/<int:pk>/',user_views.LikePost, name = 'like'), 
    path('userlike/<int:pk>/', user_views.UserLikePost, name = 'userlike'),
    path('usercomment/<int:pk>/', user_views.UserCommentPostView, name = 'usercomment'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'design/logout.html'), name = 'logout'),
    path('login/',auth_views.LoginView.as_view(template_name ='users/login.html'), name = 'login'),
    path('user/comment/<int:pk>/', user_views.UserCommentPostView, name = 'usercomment'),
 path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            success_url = reverse_lazy('design:password_reset_done'),
            template_name = 'design/password_reset.html'),
            name = 'password_reset'),

    path('password-reset-done/', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'design/password_reset_done.html'),name = 'password_reset_done'),
    
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            success_url = reverse_lazy('design:password_reset_complete'),
            template_name = 'design/password_reset_confirm.html'),
            name = 'password_reset_confirm'),
    
    path('password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view( template_name = 'design/password_reset_complete.html'), name = 'password_reset_complete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)