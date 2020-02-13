# coding: utf-8

import logging

from django.core.management.base import BaseCommand

from hello_activemq.mq import mq_service as mq
from hello_activemq.mq.mq_listener import MqListener

log = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'mq starts listener'

    def handle(self, *args, **options):
        log.info("mq starts")
        return mq.consume_msg(MqListener(), True)
