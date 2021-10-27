from django import forms
from django.forms import fields
from .models import Post



class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body',)



class EditPostForm(forms.ModelForm):
    # زمانی که قراره یک چیزی رو ادیت کنیم، بهتره از مدل فرم استفاده کنیم تا اینستنس رو براش بفرستیم
    # اینطوری دیگه نیاز نیست بقیه مقادیر مدل رو دستی پر کنیم، اینستنس در خودش داره
    class Meta:
        model = Post
        fields = ('body',)