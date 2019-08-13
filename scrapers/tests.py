from django.test import TestCase
from rest_framework.test import APIClient
import time

# Create your tests here.
class LoadTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_url = 'http://localhost:8000/'
        self.search_url = self.base_url + 'api/scrapers/search'
    def test_one_hundred_requests_in_five_seconds(self):
        for i in range(1,101):
            if i%25 == 0:
                time.sleep(1.25)
            res = self.client.get(self.search_url+'?key1=דודו טסה')
            self.assertTrue(res.status_code == 301)
