from django import forms
from django.forms import fields
from django.forms.widgets import Widget
from .models import Post, Comment



class AddPostForm(forms.ModelForm):
    class Meta:
        # متا کلاس های رو میتونیم به عنوان یک سری اطلاعات و ویژگی های اضافی در نظر بگیریم که بدیم به کلاس هامون
        model = Post
        fields = (
            'body',
            )



class EditPostForm(forms.ModelForm):
    # زمانی که قراره یک چیزی رو ادیت کنیم، بهتره از مدل فرم استفاده کنیم تا اینستنس رو براش بفرستیم
    # اینطوری دیگه نیاز نیست بقیه مقادیر مدل رو دستی پر کنیم، اینستنس در خودش داره
    class Meta:
        model = Post
        fields = (
            'body',
            )
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control',
                },
            ),
        }
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است',
                'max_length': 'تعداد کارکتر ها بیش از حد مجاز است',
            },
        }
        help_texts = {
            'body': 'تا 500 کاراکتر میتوانید بنویسید',
        }



class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
            )
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Write Your Comment',
                    },
                ),
            }
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است',
                'max_length': 'تعداد کارکتر ها بیش از حد مجاز است',
            },
        }
        help_texts = {
            'body': 'تا 500 کاراکتر میتوانید بنویسید',
        }



class AddReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'body',
            )
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Write Your Comment',
                    },
                ),
            }
        error_messages = {
            'body': {
                'required': 'این فیلد اجباری است',
                'max_length': 'تعداد کارکتر ها بیش از حد مجاز است',
            },
        }
        help_texts = {
            'body': 'تا 500 کاراکتر میتوانید بنویسید',
        }