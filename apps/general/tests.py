#coding=utf-8
from django.test import TestCase
from django.test.client import Client

class FlatpagesTests(TestCase):

    fixtures = ['flatpages.json', 'sites.json']
    
    def setUp(self):
        self.urls = ('/')
        self.c = Client()
        
    def test_flatpages_should_loads_correctly(self):
        """
        Статические страницы Flatpages должны корректно загружаться и
        возвращать код 200
        """аа
        for url in self.urls:
            r = self.c.get(url)
            self.assertEquals(r.status_code, 200)
            self.assertTemplateUsed(r, 'flatpages/default.html')
