from django.test import TestCase
from apps.authentication.models import CodeActivate
from django.contrib.auth.models import User

class CodeActivateModelTest(TestCase):
    def test_str_representation(self):
        user = User.objects.create(username='testuser')
        code = '12345'
        code_activate = CodeActivate(user=user, code=code)
        self.assertEqual(str(code_activate), f'{code}')
