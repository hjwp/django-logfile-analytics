from django.test import TestCase
from django.utils import timezone

from analytics.models import Hit

class HitModelTest(TestCase):
    def test_defaults(self):
        h = Hit()
        self.assertEqual(h.source_ip, '')
        self.assertEqual(h.timestamp, None)
        self.assertEqual(h.method, '')
        self.assertEqual(h.url, '')
        self.assertEqual(h.status_code, None)
        self.assertEqual(h.response_size, None)
        self.assertEqual(h.referer_url, None)
        self.assertEqual(h.user_agent, '')

    def test_only_timestamp_and_status_code_required(self):
        h = Hit()
        h.timestamp = timezone.now()
        h.status_code = 451
        h.save()

