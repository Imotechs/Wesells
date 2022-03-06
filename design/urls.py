from django.urls import path,reverse_lazy
from .import views
from django.contrib.auth import views as auth_views
from .views import (HomeListView,updateItems,
LadiesDetailView,
CarsView,
HandbagView,
ShoesView,
PostDelete,
PostDetails,
PostUpdate,
CreatePostView,
UserPostUpdate,
UserPostDelete,
CreateChildrenView,
CreateLadyView,
CreatePhoneView,
CreateHandBagView,
CreateCarView,
CreateShoeView,
ChildrenDetailView,
PhoneView
)
from users.views import (
    BlogPostViw,
    PlaceOdderFormView,
    DashbaordView,
    Homeplaceorder,
    UserCreatePostView,

)

from django.conf import settings
from django.conf.urls.static import static


app_name = 'design'

urlpatterns = [
    path('', views.Home, name = 'index'),
    path('update_item/', views.updateItems,name = 'updateitem'),
    path('blog/', BlogPostViw.as_view(), name = 'blog'),
    path('order/<int:pk>/', PlaceOdderFormView.as_view(), name = 'placeorder'),
    path('dashboard/',DashbaordView.as_view(), name = 'dashboard'),
    path('ordering/', Homeplaceorder.as_view(), name = 'ordering'),
    path('about/', views.about, name = 'about'), 
    path('makepost/',UserCreatePostView.as_view(), name = 'makepost'),
    path('children/',CreateChildrenView.as_view(), name = 'children' ),
    path('children/detail/<int:pk>/', ChildrenDetailView.as_view(), name ='childdetails'),  
    path('ladies/detail/<int:pk>/', LadiesDetailView.as_view(), name ='ladydetails'),  
    path('lady/',CreateLadyView.as_view(), name = 'lady' ),  
    path('new-post/',CreatePostView.as_view(), name = 'create'),  
    path('details/<int:pk>/',PostDetails.as_view(), name = 'details'),  
    path('update/<int:pk>/',PostUpdate.as_view(), name = 'update'),  
    path('userpostupdate/<int:pk>/',UserPostUpdate.as_view(), name = 'userupdate'),  
    path('delete/<int:pk>/',PostDelete.as_view(), name = 'delete'),
    path('post_phone/', CreatePhoneView.as_view(), name = 'postphone'),
    path('post_shoe/', CreateShoeView.as_view(), name = 'postshoe'),
    path('post_car/', CreateCarView.as_view(), name = 'postcar'),
    path('post_handbag/', CreateHandBagView.as_view(), name = 'posthandbag'),

    path('User/Delete/post/<int:pk>/', UserPostDelete.as_view(), name = 'userdelete'),
    path('cars/', CarsView.as_view(), name ='cars' ),
    path('phones/', PhoneView.as_view(), name ='phones' ),
    path('handbag/', HandbagView.as_view(), name ='handbags' ),
    path('shoes/', ShoesView.as_view(), name ='shoes' ),

  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)