from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """test email successful"""
        email = 'rahmad@umarta.dev'
        password = 'mamakmu'
        user = get_user_model().object.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test email for new user is normalized"""

        email = 'test@UMARTA.DEV'
        user = get_user_model().object.create_user(email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """create user with no email"""

        with self.assertRaises(ValueError):
            get_user_model().object.create_user(None, 'test1234')
