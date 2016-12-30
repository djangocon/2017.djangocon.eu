from django.test import TestCase
import datetime
from .views import is_cfp_closed


class CFP_TestCases(TestCase):
    def test_closing_date_tomorrow(self):
        test_date = datetime.date.today() + datetime.timedelta(days=1)
        with self.settings(CFP_CLOSING_DATE=test_date.strftime("%Y-%m-%d")):
            self.assertFalse(is_cfp_closed())

    def test_closing_date_same_date(self):
        test_date = datetime.date.today()
        with self.settings(CFP_CLOSING_DATE=test_date.strftime("%Y-%m-%d")):
            self.assertTrue(is_cfp_closed())

    def test_closing_date_yesterday(self):
        test_date = datetime.date.today() - datetime.timedelta(days=1)
        with self.settings(CFP_CLOSING_DATE=test_date.strftime("%Y-%m-%d")):
            self.assertTrue(is_cfp_closed())
