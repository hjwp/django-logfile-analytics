import os
import platform
try:
    from pyvirtualdisplay import Display
except ImportError:
    pass
from selenium import webdriver

from django.test import LiveServerTestCase



class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        if platform.system() == 'Linux' and 'DISPLAY' not in os.environ:
            Display(size=(1024,768)).start()

    def tearDown(self):
        self.browser.quit()


    def _get_body_text(self):
        return self.browser.find_element_by_tag_name('body').text


    def test_main_analytics_page_has_total_hits(self):
        self.browser.get(self.live_server_url + '/analytics/')

        self.assertIn('Hits', self._get_body_text())


