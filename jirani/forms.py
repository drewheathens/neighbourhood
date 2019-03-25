from django import forms
from .models import Business,Profile,Post,Comment

# class notificationsForm(forms.ModelForm):
#     class Meta:
#         model=notifications
#         exclude=['author','neighborhood','post_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['username','neighbourhood','avatar']

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        exclude=['owner','neighbourhood']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
