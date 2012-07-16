from datetime import datetime
from django.test import TestCase

from analytics.models import Hit
from analytics.parser import parse_logfile

class HitModelTest(TestCase):
    def test_defaults(self):
        h = Hit()
        self.assertEqual(h.source_ip, '')
        self.assertEqual(h.timestamp, None)
        self.assertEqual(h.method, '')
        self.assertEqual(h.url, '')
        self.assertEqual(h.status_code, None)
        self.assertEqual(h.response_size, None)
        self.assertEqual(h.referer_url, '')
        self.assertEqual(h.user_agent, '')


class ParserTest(TestCase):

    def test_parsing_a_logfile(self):
        filename = 'test_log_data_small.log'
        parse_logfile(filename)
        self.assertEqual(Hit.objects.all().count(), 3)
        self.assertEqual(Hit.objects.all(), Hit.objects.all().order_by('timestamp'))

        hit1 = Hit.objects.all()[0]
        self.assertEqual(hit1.source_ip, '78.86.125.186')
        self.assertEqual(hit1.timestamp, datetime('2011-07-21 17:49:33'))
        self.assertEqual(hit1.method, 'GET')
        self.assertEqual(hit1.url, '/')
        self.assertEqual(hit1.status_code, 500)
        self.assertEqual(hit1.response_size, 404)
        self.assertEqual(hit1.referer_url, 'http://www.pythonanywhere.com/user/harry/webapps/')
        self.assertEqual(hit1.user_agent, 'Mozilla/5.0 (Windows NT 6.0; rv:6.0.2) Gecko/20100101 Firefox/6.0.2')


        hit2 = Hit.objects.all()[1]
        self.assertEqual(hit2.source_ip, '78.86.125.186')
        self.assertEqual(hit2.timestamp, datetime('2011-07-21 18:11:19'))
        self.assertEqual(hit2.method, 'POST')
        self.assertEqual(hit2.url, '/accounts/login/')
        self.assertEqual(hit2.status_code, 200)
        self.assertEqual(hit2.response_size, 744)
        self.assertEqual(hit2.referer_url, 'http://www.pythonanywhere.com/')
        self.assertEqual(hit2.user_agent, 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1')


        hit3 = Hit.objects.all()[2]
        self.assertEqual(hit3.source_ip, '66.249.71.146')
        self.assertEqual(hit3.timestamp, datetime('2012-05-07 17:49:33'))
        self.assertEqual(hit3.method, 'GET')
        self.assertEqual(hit3.url, 'static/images/admin03t.png')
        self.assertEqual(hit3.status_code, 304)
        self.assertEqual(hit3.response_size, None)
        self.assertEqual(hit3.referer_url, None)
        self.assertEqual(hit3.user_agent, 'Googlebot-Image/1.0')



    def test_parsing_single_line(self):
        line = '78.86.125.186 - - [21/Sep/2011:17:26:56 +0000] "GET / HTTP/1.1" 500 404 "http://www.pythonanywhere.com/user/harry/webapps/" "Mozilla/5.0 (Windows NT 6.0; rv:6.0.2) Gecko/20100101 Firefox/6.0.2"'
        self.fail('todo')
