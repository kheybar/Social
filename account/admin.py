from django.contrib import admin
from django.contrib.auth.admin import UserAdmin # ظاهر ادمین که در قسمت ادمین مشاهده میکنیم
from django.contrib.auth.models import User
from .models import Profile


# اینلاین یک قرارداد بین برنامه نویسان است
class ProfileInline(admin.StackedInline): # برای تعیین نحوه نمایش در ادمین جنگو از این کلاس ارث بری میکنه
    model = Profile
    can_delete = False # کسی نتونه از طریق پنل ادمین حذفش کنه


class ExtendedProfileAdmin(UserAdmin): # برای برقراری ارتباط با با پنل ادمین از این کلاس ارث بری میکنه
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(User, ExtendedProfileAdmin)