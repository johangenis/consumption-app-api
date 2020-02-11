from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Consumption_type

from consumption.serializers import Consumption_typeSerializer


CONSUMPTION_TYPE_URL = reverse("consumption:consumption_type-list")


class PublicConsumption_typeApiTests(TestCase):
    """Test the publicly available consumption type API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login required for retrieving consumption type"""
        res = self.client.get(CONSUMPTION_TYPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateConsumption_typeApiTests(TestCase):
    """Test the authorized user consumption type API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@artil.com", "password"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_consumption_types(self):
        """Test retrieving consumption type"""
        Consumption_type.objects.create(user=self.user, cons_type="Rain")
        Consumption_type.objects.create(
            user=self.user, cons_type="Electricity"
        )

        res = self.client.get(CONSUMPTION_TYPE_URL)

        consumption_type = Consumption_type.objects.all().order_by(
            "-cons_type"
        )
        serializer = Consumption_typeSerializer(consumption_type, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_consumption_types_limited_to_user(self):
        """Test that consumption type returned are for authenticated user"""
        user2 = get_user_model().objects.create_user(
            "other@artil.com", "testpass"
        )
        Consumption_type.objects.create(user=user2, cons_type="Food")
        consump_type = Consumption_type.objects.create(
            user=self.user, cons_type="Water"
        )

        res = self.client.get(CONSUMPTION_TYPE_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["cons_type"], consump_type.cons_type)

    def test_create_consumption_type_successful(self):
        """Test creating a new consumption type"""
        payload = {"cons_type": "Simple"}
        self.client.post(CONSUMPTION_TYPE_URL, payload)

        exists = Consumption_type.objects.filter(
            user=self.user, cons_type=payload["cons_type"]
        ).exists()
        self.assertTrue(exists)

    def test_create_consumption_type_invalid(self):
        """Test creating a new consumption type with invalid payload"""
        payload = {"cons_type": ""}
        res = self.client.post(CONSUMPTION_TYPE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
