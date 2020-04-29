# coding: utf-8
import logging

from django.core.management.base import BaseCommand

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Hello Command'

    def handle(self, *args, **options):
        log.info("Hello Command.")
