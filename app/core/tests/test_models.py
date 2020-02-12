from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@agil.com", password="testpass"):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = "test@artil.com"
        password = "Password123"
        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@ARTIL.com"
        user = get_user_model().objects.create_user(email, "test123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@artil.com", "test123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_consumption_type_str(self):
        """Test the consumption type string representation"""
        consumption_type = models.Consumption_type.objects.create(
            user=sample_user(), cons_type="Electricity"
        )

        self.assertEqual(str(consumption_type), consumption_type.cons_type)

    # def test_consumption_record_str(self):
    #     """Test the consumption record string representation"""
    #     consumption_record = models.Consumption_record.objects.create(
    #         user=sample_user(),
    #         consumption_record.cons_type="Water",
    #         # cons_type.set("Water"),
    #         date_time="2020-02-12",
    #         amount=5.00,
    #     )

    #     self.assertEqual(str(consumption_record), \
    #       consumption_record.cons_type)
