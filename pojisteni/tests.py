from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Insured

class InsuredModelTest(TestCase):
    def setUp(self):
        Insured.objects.create(name="Test Name", address="Test Address")

    def test_insured_str(self):
        insured = Insured.objects.get(name="Test Name")
        self.assertEqual(str(insured), "Name: Test Name | Address: Test Address | Email:  | Phone: ")
