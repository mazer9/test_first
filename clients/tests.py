from rest_framework.test import APITestCase

from clients.models import Client


class TestFileUpload(APITestCase):
    fixtures = ['clients.json', 'items.json', 'deals.json', ]

    def test_get_gems(self):
        self.assertEqual(('Камень',), Client.objects.first().get_gems)
