# در تست کردن یوآرال مهم اینه که اون چیزی که میخوایم حتما به ویویی که داره، بره


from django.test import SimpleTestCase # چون کاری با دیتابیس نداریم از سیمپل استفاده میکنیم
from django.urls import reverse, resolve
from account.views import (
    user_login,
    user_dashboard,
    phone_login,
    phone_login_verify,
    user_register,
    user_logout,
    profile_edit,

)



class TestUrl(SimpleTestCase):
    def test_login(self):
        url = reverse('account:login') # output => /account/login/
        # print(resolve(url)) # output => ResolverMatch(func=account.views.user_login, args=(), kwargs={}, url_name=login, app_names=['account'], namespaces=['account'], route=account/login/)
        self.assertEqual(resolve(url).func, user_login)


    def test_phone_login(self):
        url = reverse('account:phone_login')
        self.assertEqual(resolve(url).func, phone_login)

    
    def test_phone_login_verify(self):
        url = reverse('account:phone_login_verify')
        self.assertEqual(resolve(url).func, phone_login_verify)


    def test_user_register(self):
        url = reverse('account:register')
        self.assertEqual(resolve(url).func, user_register)

    
    def test_user_logout(self):
        url = reverse('account:logout')
        self.assertEqual(resolve(url).func, user_logout)


    def test_user_dashboard(self):
        url = reverse('account:dashboard', args=('1',)) # send args because get user_id
        self.assertEqual(resolve(url).func, user_dashboard)


    def test_profile_edit(self):
        url = reverse('account:profile_edit', args=('1',)) # send args because get user_id
        self.assertEqual(resolve(url).func, profile_edit)