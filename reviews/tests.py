from django.test import TestCase

# Create your tests here.
from .models import Review

class ReviewTestCase(TestCase):
    
    def test_queryset_exists(self):
        qs = Review.objects.all()
        self.assertTrue(qs.exists())
        

