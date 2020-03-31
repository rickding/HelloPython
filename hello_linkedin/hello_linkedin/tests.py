import logging

from django.test import TestCase

log = logging.getLogger(__name__)


class HelloTest(TestCase):
    def test_log(self):
        log.info('Hello Test!')
