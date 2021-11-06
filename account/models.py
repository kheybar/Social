"""

    برای توسعه مدل یوز جنگو از روش وان تو وان پیرو روش زیر عمل میکنیم
    بعد از تعیین رابطه، مواردی که میخوایم اضافه بشه به مدل یوزر جنگو مینویسیم
    برای اضافه کردن پروفایل به هر کاربر میتونیم زمان ثبت نام این کارو انجام بدیم یا از روش تمیز تر سیگنال استفاده کنیم
    
    سیگنال: در برنامه یک اتفاقی می افته، بعد میخوایم یک سیگنالی بفرستیم به یک قسمت دیگه ای
    از برناممون و برنامه یک کار خاصی انجام بده
    یکی از خوبیاش اینه که یک سری اطلاعات مفید هم میده از فرستنده سیگنال
    مثال سیگنال: زمانی که کاربر میاد و پست یک نفر رو لایک میکنه، یک نوتیف برای صاحب پست بره
    ما سیگنال های متفاوتی داریم:
    یک-پری سیو: اگر احیانا در مدل چیزی خواست سیو بشه، قبل از سیو شدن، به من خبر بده
    دو-پست سیو: بعد از سیو شدن به من خبر بدايته
    سه-پری دلیلت: میگه اگر چیزی از مدل خواست حذف بشه، قبل از حذف شدن به من خبر بده
    چهار-پست دلیلت: بعد از حذف شدن به من خبر بده
    پنج-ام۲ام چینج: اگر رابطه منی تو منی فرق کرد به من خبر بده
    شش-ریکوئست استارت: اگر ریکوئست خاصی شروع شد به من خبر بده
    هفت-ریکوئست فنش: اگر اون ریکوئست خاص تموم شد به من خبر بده

    الان ما زمانی که کاربری ذخیره شد میخوایم بیایم و براش پروفایل رو هم ذخیره کنیم،
    پس از سیگنال پست سیو استفاده میکنیم

    روش استفاده از سیگنال:
    روش اول: استفاده از فانکشن کانکت
    روش دوم: استفاده از دکوریتور ریسور
    فرقی هم نمیکنه

"""


from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone = models.PositiveSmallIntegerField(null=True, blank=True)


    def __str__(self):
        return self.user.username




def save_profile(sender, **kwargs): # سندر رو حتما باید بهش بدیم. کیوردآرگس حاوی یک سری اطلاعات است: کریتد که یک بولین هست و میگه آیا ساخته شد و دوم اینستنس هست که در واقع همون یوزر رو اتومات میفرسته برامون
    if kwargs['created']: # آیا با موفقیت ذخیره شد
        p1 = Profile(user=kwargs['instance']) # آبجکتی که ذخیره شد در مدل یوزر


# یوزر به محض اینکه ی اتفاقی افتاد براش، ی سیگنال بفرست به متود سیو پروفایل و میاد این متود رو ران میکنه
post_save.connect(receiver=save_profile, sender=User) # مرتب حواسش به مدل یوزر هست که چیزی ذخیره میشه یا نه



class Relational(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.from_user} following {self.to_user}'