from django import forms
from .models import BlogPost, Category, Comment, Profile


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('auth_user', 'category','image', 'body')

        widgets = {
            'auth_user': forms.TextInput(attrs={
                'id':'add',
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'User',
                'value': '',
                'type': 'hidden',

            }),
            'category': forms.Select(choices=choice_list, attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Category',
                'default': 'Coding',
            }),
            'body': forms.Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Write Something'
            }),
            
        }

        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('auth_user', 'image', 'body')

        widgets = {
            'auth_user': forms.Select(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'User'
            }),
            'body': forms.Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Write Something'
            }),
            
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'User',
                'id':'comm',
                'value': '',
                'type': 'hidden'
            }),
            'body': forms.Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Write Something',
                'rows': '2'
            }),
            
        }