from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Pereval, Coords, User
from .serializers import PerevalSerializer


class PerevalApiTestCase(APITestCase):

    def setUp(self):
        user_1 = User.objects.create(email='Testt', phone=+77777777, fam='Testt', name='Testt', otc='Testt')
        user_2 = User.objects.create(email='Testtt', phone=+8888888, fam='Testtt', name='Testtt', otc='Testtt')
        coords_1 = Coords.objects.create(latitude=37.6767, longitude=38.6868, height=1250)
        coords_2 = Coords.objects.create(latitude=39.6969, longitude=40.6060, height=2500)
        self.pereval_1 = Pereval.objects.create(user=user_1, beautyTitle='beautyTitlet', title="titlet",
                                                other_titles='other_titlest', coords=coords_1)
        self.pereval_2 = Pereval.objects.create(user=user_2, beautyTitle='beautyTitlett', title="titlett",
                                                other_titles='other_titlestt', coords=coords_2)

    def test_get_list(self):
        url = reverse('SubmitData-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(len(serializer_data), 2)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_get_detail(self):
        url = reverse('SubmitData-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)


class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        user_1 = User.objects.create(email="T", phone=1111, fam="Test1", name="Test1", otc="Test1")
        user_2 = User.objects.create(email="Testtt@mail.ru", phone=2222, fam="Testtt", name="Testtt", otc="Testtt")
        coords_1 = Coords.objects.create(latitude=37.6767, longitude=38.6868, height=1250)
        coords_2 = Coords.objects.create(latitude=39.6969, longitude=40.6060, height=2500)
        self.pereval_1 = Pereval.objects.create(user=user_1, beautyTitle="beautyTitlet", title="titlet",
                                                other_titles="other_titlest",
                                                coords=coords_1)
        self.pereval_2 = Pereval.objects.create(user=user_2, beautyTitle='beautyTitlett', title="titlett",
                                                other_titles='other_titlestt', coords=coords_2)

    def test_check(self):
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2], many=True).data

        expected_data = [
            {
                "id": 1,
                "user": {
                    "fam": "Test1",
                    "name": "Test1",
                    "otc": "Test1",
                    "email": "T",
                    "phone": 1111
                },
                "coords": {
                    "id": 1,
                    "latitude": 37.6767,
                    "longitude": 38.6868,
                    "height": 1250
                },
                "level": None,
                "images": None,
                "beautyTitle": "beautyTitlet",
                "title": "titlet",
                "other_titles": "other_titlest",
                "connect": None,
                "add_time": None,
                "status": None,
            },
            {
                "id": 2,
                "user": {
                    "fam": "Test1",
                    "name": "Test1",
                    "otc": "Test1",
                    "email": "T",
                    "phone": 1111
                },
                "coords": {
                    "id": 2,
                    "latitude": 39.6969,
                    "longitude": 40.6060,
                    "height": 2500
                },
                "level": None,
                "images": None,
                "beautyTitle": "beautyTitlet",
                "title": "titlet",
                "other_titles": "other_titlest",
                "connect": None,
                "add_time": None,
                "status": None,
            },
        ]

        self.assertEqual(serializer_data, expected_data)
