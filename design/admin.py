from django.contrib import admin
from .models import (Post,Comment,
                Lady,Children, 
                Car,Handbag,Shoe,
                Order,OrderItem,
            
)
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Lady)
admin.site.register(Children)
admin.site.register(Car)
admin.site.register(Shoe)
admin.site.register(Handbag)
admin.site.register(OrderItem)
admin.site.register(Order)