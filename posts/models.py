"""

    بکوارد ریلیشن:
    برای اینکه از مدل کامنت به پست ها دسترسی داشته باشیم خیلی راحت انجام میشه
    اما اگر بخوایم از پست ها به کامنت ها دسترسی داشته باشیم باید از بکوارد ریلیشن استفاده کنیم
    زمانی که بخوایم برعکس به مدل دسترسی داشنه باشیم از آندلاین ست استفاده می‌کنیم
    این روش برای تمام روابط کار میکنه به جز وان تو وان که نیاز به نوشتن آندرلاین ست نداره
    ما بدون استثنا از آندرلاین ست استفاده نمی کنیم، ظاهر زیبایی هم نداره
    برای تغییرش، به فیلدمون یدونه ریلیتد نیم اضافه میکنیم و دیگه از اون اسم استفاده میکنیم
    این برای زمانی کار میکنه که بخوایم برعکس داخل رابطه حرکت کنیم

    اگر بخوایم کاری کنیم که نشه بصورت برعکس داخل رابطه حرکت کرد، در ریلیتد نیم یک علامت مثبت میزاریم


"""




from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    slug = models.SlugField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return f'{self.user}-{self.body[:25]}' # بادی رو تا 25 کاراکتر نمایش بده

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.body[:30])
        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('posts:post_detail', args=(
            self.created.year,
            self.created.month,
            self.created.day,
            self.slug,
        ))




class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ucomment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomment')
    reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='rcomment') # برای اینکه کامنت های تو در تو داشته باشیم باید به خود مدل ربطش بدیم و از سلف در کوتیشن استفاده میکنیم تا پایتون گیر نده
    is_reply = models.BooleanField(default=False) # The default form widget for this field is CheckboxInput, or NullBooleanSelect if null=True.
    body = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)



    class Meta:
        # db_table = 'Comment' # تغییر نام تیبل در دیتابیس
        ordering = ('-created',) # تغییر تریب اطلاعات از داخل مدل(اگر تکست رو هدف قرار بدیم، بر اساس حروف الفبا کار میکنه)
        # unique_together = [['a', 'b']] # زمانی که بخوایم دوتا چیز با هم یکی باشند



    def __str__(self):
        return f'{self.user}-{self.body}'


