from django.forms import DateField, DateInput, NumberInput, TextInput, Textarea, EmailInput, PasswordInput, EmailField, CharField, ModelForm, Select
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from theblog.models import Profile, About

class UserRegisterForm(UserCreationForm):
    email = EmailField(widget = EmailInput(attrs={ 
        'class':'form-control', 
        'style': 'max-width: 300px',
        'placeholder': 'Email'
        }))
    first_name = CharField(widget = TextInput(attrs={
        'class':"form-control",
        'style': 'max-width: 300px',
        'placeholder': 'First name'
    }))
    
    last_name = CharField(widget = TextInput(attrs={
        'class':"form-control",
        'style': 'max-width: 300px',
        'placeholder': 'Last name'
    }))

    class Meta:
        model = User

        fields = ('username','email','first_name','last_name','password1','password2')
        
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'max-width: 300px'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['style'] = 'max-width: 300px'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['style'] = 'max-width: 300px'
        self.fields['password2'].widget.attrs['placeholder'] = 'Comfirm Password'
        
        
class EditProfileForm(UserChangeForm):
    email = EmailField(widget = EmailInput(attrs={ 
        'class':'form-control', 
        'style': 'max-width: 300px',
        'placeholder': 'Email'
        }))
    first_name = CharField(widget = TextInput(attrs={
        'class':"form-control",
        'style': 'max-width: 300px',
        'placeholder': 'First name'
    }))
    
    last_name = CharField(widget = TextInput(attrs={
        'class':"form-control",
        'style': 'max-width: 300px',
        'placeholder': 'Last name'
    }))

    class Meta:
        model = User

        fields = ('username','email','first_name','last_name')
        
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'max-width: 300px'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
       
        
class UserLoginForm(UserCreationForm):
    

    class Meta:
        model = User

        fields = ('username','password')
        
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['style'] = 'max-width: 300px'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['style'] = 'max-width: 300px'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        
class PasswordChangingForm(PasswordChangeForm):
    
    class Meta:
        model = User
        fields = ('old_password','new_password1', 'new_password2')
        labels = {'old_password':'','new_password1':'', 'new_password2':''}
    old_password = CharField(widget = PasswordInput(attrs={ 
        'class':'form-control', 
        'style': 'max-width: 300px',
        'placeholder': 'Old password',
        'label':''
        }))
    new_password1 = CharField(widget = PasswordInput(attrs={
        'class':"form-control",
        'style': 'max-width: 300px',
        'placeholder': 'New password'
    }))
    
    new_password2 = CharField(widget = PasswordInput(attrs={
        'class':"form-control",
        'style': 'max-width: 300px',
        'placeholder': 'Confirm new password'
    }))

class ProfilePageForm(ModelForm):
    class Meta:
        model = Profile

        fields = ('image','linkedIn_url', 'twitter_url','instagram_url', 'facebook_url')

        widgets = {
            'linkedIn_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'LinkedIn',

            }),'twitter_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Twitter',

            }),'instagram_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Instagram',

            }),'facebook_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Facebook'
            }),
            
        }
        
class EditProfilePageForm(ModelForm):
    class Meta:
        model = Profile

        fields = ('image','linkedIn_url', 'twitter_url','instagram_url', 'facebook_url')

        widgets = {
            'linkedIn_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'LinkedIn',

            }),'twitter_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Twitter',

            }),'instagram_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Instagram',

            }),'facebook_url': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Facebook'
            }),
            
        }

class AboutPageForm(ModelForm):
    class Meta:
        model = About
        FREELANCE_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
        ]

        fields = ('birthday','age', 'skill_1','skill_2', 'bio', 'description', 'website', 'degree', 'phone', 'city', 'freelance', 'about_image')

        widgets = {
            'birthday': DateInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Birthday',
                'type':'date'

            }),'age': NumberInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Age',

            }),'skill_1': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Your Skill',

            }),'skill_2': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Second Skill'

            }),'bio': Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Bio',
                'rows':'2',

            }),'description': Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Description',
                'rows':'2',

            }),'website': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Website',

            }),'degree': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Education degree',

            }),'phone': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Phone',
                'type': 'tel',

            }),'city': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'City',

            }),'freelance': Select(choices = FREELANCE_CHOICES, attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Freelance'
            }),
            
        }

class EditAboutForm(ModelForm):
    class Meta:
        model = About
        FREELANCE_CHOICES = [
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
        ]

        fields = ('birthday','age', 'skill_1','skill_2', 'bio', 'description', 'website', 'degree', 'phone', 'city', 'freelance', 'about_image')

        widgets = {
            'birthday': DateInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Birthday',
                'type':'date'

            }),'age': NumberInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Age',

            }),'skill_1': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Your Skill',

            }),'skill_2': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Second Skill'

            }),'bio': Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Bio',
                'rows':'2',

            }),'description': Textarea(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Description',
                'rows':'2',

            }),'website': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Website',

            }),'degree': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Education degree',

            }),'phone': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Phone',
                'type': 'tel',

            }),'city': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'City',

            }),'freelance': Select(choices = FREELANCE_CHOICES, attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Freelance'
            }),
            
        }
