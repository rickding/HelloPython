# -*-coding:utf-8-*-
import logging
import time

import stomp

log = logging.getLogger(__name__)


def send_msg_to_queue(msg):
    conn = stomp.Connection10()
    conn.connect()
    conn.send('SampleQueue', 'Simples Assim')
    conn.disconnect()


class SampleListener(object):
    def on_message(self, headers, msg):
        log.info('[%s]received a message %s' % (msg, time.strftime("%Y-%m-%d %H:%M:%S")))
        log.info(msg)
        log.info(headers)

    def on_error(self, headers, msg):
        log.info('[%s]received an error %s' % (msg, time.strftime("%Y-%m-%d %H:%M:%S")))
        log.info('headers: ')
        log.info(headers)


def recv_msg_from_queue():
    conn = stomp.Connection10()
    conn.set_listener('SampleListener', SampleListener())
    conn.connect()
    conn.subscribe('SampleQueue')
    while 1:
        time.sleep(1)  # secs

    conn.disconnect()
