# coding: utf-8

import logging

from django.core.management.base import BaseCommand

from hello_activemq.service import mq_service as mq

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'mq starts listener'

    def handle(self, *args, **options):
        log.info("mq starts")
        return mq.recv_msg_from_queue()
