from django.test import TestCase
from django.utils import timezone

from analytics.models import Hit

class HomePageTest(TestCase):

    def test_home_page_sends_all_hits_to_template(self):
        Hit(timestamp=timezone.now(), status_code=200).save()
        Hit(timestamp=timezone.now(), status_code=200).save()
        Hit(timestamp=timezone.now(), status_code=200).save()

        response = self.client.get('/analytics/')

        self.assertTemplateUsed(response, 'home.html')

        hits_in_context = response.context['hits']
        self.assertItemsEqual(hits_in_context, Hit.objects.all())



