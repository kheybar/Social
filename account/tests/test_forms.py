# در تست کردن فرم ها ما باید دو کارا نجام بدیم: اگر اطلاعات درست اومد چیکار کنیم و اگر اطلاعات اشتباه اومد چیکار کنیم

from django.test import SimpleTestCase
from account.forms import (
    UserLoginForm,
    UserRegistarionForm,
)



class TestUserLoginForm(SimpleTestCase):
    # accepttens
    def test_valid_data(self):
        form = UserLoginForm(data={'username': 'boss', 'password': '123456'})
        self.assertTrue(form.is_valid()) # متود فرم ولید با این اطلاعاتی که من بهش دادم باید ترو برگردونه. اگر هرچیز دیگه ای بر گردوند ارور بده

    # rejection
    def test_invalid_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)



class TestUserRegistarionForm(SimpleTestCase):
    def test_valid_data(self):
        form = UserLoginForm(data={'username': 'boss', 'email': 'mahdizarepour15@gmail.com', 'password': '123456'})
        self.assertTrue(form.is_valid())

    
    def test_invalid_data(self):
        form = UserLoginForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)