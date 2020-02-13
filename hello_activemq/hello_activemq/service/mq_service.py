# -*-coding:utf-8-*-
import json
import logging
import threading
import time

import stomp
from django.conf import settings

log = logging.getLogger(__name__)


def send_msg_to_queue(msg, queue=settings.MQ_QUEUE):
    send_msg(msg, queue)


def send_msg_to_topic(msg, topic=settings.MQ_TOPIC):
    send_msg(msg, topic)


def send_msg(msg, queue_or_topic=settings.MQ_QUEUE):
    conn = get_conn()
    conn.send(queue_or_topic, msg)


class MsgListener(stomp.ConnectionListener):
    def on_message(self, headers, msg):
        log.info('Msg: %s, %s' % (msg, headers))

        msg_dict = None
        try:
            msg_dict = json.loads(msg)
        except Exception as e:
            log.warning('Exception when parse msg: %s' % str(e))

        log.info('MsgListener: {}, {}'.format(type(msg_dict), msg_dict))

    def on_error(self, headers, msg):
        log.info('Error msg: %s, %s' % (msg, headers))


def consume_msg(include_topic=False, queue=settings.MQ_QUEUE, topic=settings.MQ_TOPIC):
    conn = get_conn()
    conn.set_listener('', MsgListener())
    conn.subscribe(queue)

    if include_topic:
        conn.subscribe(topic)

    while 1:
        time.sleep(1000)  # secs

    close_conn()


mq_conn_lock = threading.Lock()
mq_conn = None


def get_conn():
    global mq_conn_lock
    global mq_conn

    if mq_conn is None or not mq_conn.is_connected():
        if mq_conn_lock.acquire():
            if mq_conn is None or not mq_conn.is_connected():
                log.warning('create mq connection')
                mq_conn = stomp.Connection10([(settings.MQ_URL, settings.MQ_PORT)])
                mq_conn.connect(settings.MQ_USER, settings.MQ_PASSWORD)

            mq_conn_lock.release()

    return mq_conn


def close_conn():
    global mq_conn_lock
    global mq_conn

    if mq_conn is not None and mq_conn.is_connected():
        if mq_conn_lock.acquire():
            if not mq_conn is None and mq_conn.is_connected():
                log.warning('close mq connection')
                mq_conn.disconnect()
                mq_conn = None

            mq_conn_lock.release()
