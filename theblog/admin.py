from django.contrib import admin
from .models import BlogPost, Category, Profile,About, Comment, Friend

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Comment)
admin.site.register(Friend)