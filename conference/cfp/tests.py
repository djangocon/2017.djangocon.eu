import datetime

from django.test import TestCase

from .views import is_cfp_closed


class CFP_TestCases(TestCase):
    def test_closing_date_tomorrow(self):
        test_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertFalse(is_cfp_closed(test_date.strftime("%Y-%m-%d")))

    def test_closing_date_same_date(self):
        test_date = datetime.date.today()
        self.assertTrue(is_cfp_closed(test_date.strftime("%Y-%m-%d")))

    def test_closing_date_yesterday(self):
        test_date = datetime.date.today() - datetime.timedelta(days=1)
        self.assertTrue(is_cfp_closed(test_date.strftime("%Y-%m-%d")))
