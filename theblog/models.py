from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        null = True,
        on_delete=models.CASCADE)
    friends = models.ManyToManyField("Friend", related_name='friend')
    linkedIn_url = models.CharField(default="",max_length=100,  blank=True, null=True)
    twitter_url = models.CharField(default="",max_length=100,  blank=True, null=True)
    instagram_url = models.CharField(default="",max_length=100,  blank=True, null=True)
    facebook_url = models.CharField(default="",max_length=100,  blank=True, null=True)
    image = models.ImageField(upload_to = 'images/profile', null=True, blank=True )
    verified = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='profile', null=True, blank = True, default='')

    def __str__(self):
        return str(self.profile)

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.body
    

class About(models.Model):
    user = models.OneToOneField(
        User,
        null = True,
        on_delete=models.CASCADE)
    FREELANCE_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    ]
    birthday = models.DateField(default= "2000-12-31" ,max_length=200, blank=True, null=True)
    age = models.PositiveIntegerField(default="20",  blank=True, null=True)
    skill_1 = models.CharField(default= "" ,max_length=200, blank=True, null=True)
    skill_2 = models.CharField(default= "" ,max_length=200, blank=True, null=True)
    bio = models.CharField(default= "" ,max_length=200, blank=True, null=True)
    description = models.CharField(default="",max_length=200,  blank=True, null=True)
    website     = models.CharField(default="", max_length=200,  blank=True, null=True)
    degree = models.CharField(default="",max_length=100,  blank=True, null=True)
    phone = models.CharField(default="",max_length=100,  blank=True, null=True)
    city = models.CharField(default="",max_length=100,  blank=True, null=True)
    freelance = models.CharField(max_length=20, default="Unavailable")
    about_image = models.ImageField(upload_to = 'about_images', null=True, blank=True )
    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class BlogPost(models.Model):
    auth_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    category = models.CharField(max_length=255, default = 'coding')
    body=models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name = 'blog_posts')
    image = models.ImageField(null = True, blank = True, upload_to = 'images')
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return  '%s - %s' % (str(self.auth_user), self.body)
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s -%s' % (str(self.post.auth_user), self.post.body, self.name)