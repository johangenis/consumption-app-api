from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Consumption_record, Consumption_type

import datetime

# from consumption.serializers import Consumption_recordDetailSerializer
CONSUMPTION_RECORD_URL = reverse("consumption:consumption_record-list")


def sample_consumption_type(user, cons_type="Water"):
    """Create and return a sample consumption type"""
    return Consumption_type.objects.create(user=user, cons_type=cons_type)


def detail_url(consumption_record_id):
    """Return consumption record detail URL"""
    return reverse(
        "consumption:consumption_record-detail", args=[consumption_record_id]
    )


# def sample_consumption_record(user, **params):
#     """Create and return a sample consumption record"""
#     defaults = {
#         "cons_type": "Sample consumption record",
#         "date_time": datetime.date.today(),
#         "amount": 5.00,
#     }
#     defaults.update(params)

#     return Consumption_record.objects.create(user=user, **defaults)


class PublicConsumption_recordApiTests(TestCase):
    """Test unauthenticated consumption record API access"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authenticaiton is required"""
        res = self.client.get(CONSUMPTION_RECORD_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateConsumption_recordApiTests(TestCase):
    """Test authenticated consumption record API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "test@artil.com", "testpass"
        )
        self.client.force_authenticate(self.user)

    # def test_create_basic_consumption_record(self):
    #     """Test creating consumption_record"""
    #     payload = {
    #         "cons_type": "Test consumption_record",
    #         "date_time": datetime.date.today(),
    #         "amount": 10.00,
    #     }
    #     res = self.client.post(CONSUMPTION_RECORD_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     consumption_record = \
    # Consumption_record.objects.get(id=res.data["id"])
    #     for key in payload.keys():
    #         self.assertEqual(payload[key], getattr(consumption_record, key))

    # def test_create_consumption_record_with_consumption_types(self):
    #     """Test creating consumption_record with consumption_types"""
    #     consumption_type1 = sample_consumption_type(
    #         user=self.user, cons_type="consumption_type 1"
    #     )
    #     consumption_type2 = sample_consumption_type(
    #         user=self.user, cons_type="consumption_type 2"
    #     )
    #     payload = {
    #         # "cons_type": "Test consumption_record with consumption_types",
    #         "cons_type": [consumption_type1.id, consumption_type2.id],
    #         "date_time": datetime.date.today(),
    #         "amount": 15.00,
    #     }

    #     res = self.client.post(CONSUMPTION_RECORD_URL, payload)

    #     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    #     consumption_record = \
    # Consumption_record.objects.get(id=res.data["id"])
    #     cons_type = consumption_record.consumption_types.all()
    #     self.assertEqual(cons_type.count(), 2)
    #     self.assertIn(consumption_type1, cons_type)
    #     self.assertIn(consumption_type2, cons_type)

    # def test_retrieve_consumption_records(self):
    #     """Test retrieving list of consumption records"""
    #     sample_consumption_record(user=self.user)
    #     sample_consumption_record(user=self.user)

    #     res = self.client.get(CONSUMPTION_RECORD_URL)

    #     consumption_records = \
    # Consumption_record.objects.all().order_by("-id")
    #     serializer = Consumption_recordSerializer(
    #         consumption_records, many=True
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(res.data, serializer.data)

    # def test_consumption_records_limited_to_user(self):
    #     """Test retrieving consumption records for user"""
    #     user2 = \
    # get_user_model().objects.create_user("other@artil.com", "pass")
    #     sample_consumption_record(user=user2)
    #     sample_consumption_record(user=self.user)

    #     res = self.client.get(CONSUMPTION_RECORD_URL)

    #     consumption_records = \
    # Consumption_record.objects.filter(user=self.user)
    #     serializer = Consumption_recordSerializer(
    #         consumption_records, many=True
    #     )
    #     self.assertEqual(res.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(res.data), 1)
    #     self.assertEqual(res.data, serializer.data)


def test_create_basic_consumption_record(self):
    """Test creating consumption_record"""
    payload = {
        "cons_type": "Test consumption_record",
        "date_time": datetime.date.today(),
        "amount": 10.00,
    }
    res = self.client.post(CONSUMPTION_RECORD_URL, payload)

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    consumption_record = Consumption_record.objects.get(id=res.data["id"])
    for key in payload.keys():
        self.assertEqual(payload[key], getattr(consumption_record, key))


# def test_create_consumption_record_with_consumption_type(self):
#     """Test creating consumption_record with consumption types"""
#     consumption_type1 = sample_consumption_record(
#         user=self.user, name="Consumption Type 1"
#     )
#     consumption_type2 = sample_consumption_record(
#         user=self.user, name="Consumption Type 2"
#     )
#     payload = {
#         "cons_type": "Test consumption_record with consumption_types",
#         "date_time": datetime.date.today(),
#         "price": 15.00,
#     }

#     res = self.client.post(CONSUMPTION_RECORD_URL, payload)

#     self.assertEqual(res.status_code, status.HTTP_201_CREATED)
#     consumption_record = Consumption_record.objects.get(id=res.data["id"])
#     consumption_records = consumption_record.consumption_types.all()
#     self.assertEqual(consumption_records.count(), 2)
#     self.assertIn(consumption_type1, consumption_records)
#     self.assertIn(consumption_type2, consumption_records)


# def test_view_consumption_record_detail(self):
#     """Test viewing a consumption record's detail"""
#     consumption_record = sample_consumption_record(user=self.user)
#     consumption_record.consumption_type.add(
#         sample_consumption_type(user=self.user)
#     )

#     url = detail_url(consumption_record.id)
#     res = self.client.get(url)

#     serializer = Consumption_recordDetailSerializer(consumption_record)
#     self.assertEqual(res.data, serializer.data)
