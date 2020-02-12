from __future__ import absolute_import, unicode_literals

import json
import logging
import time

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def celery_demo_task(param_dict):
    logger.info('foot task start! param_dict:%s' % param_dict)
    time.sleep(5)
    return 'finished'


@shared_task
def celery_demo_task2(param_dict):
    logger.info('foot task start! param_dict:%s' % param_dict)
    time.sleep(5)
    return 'finished'


@shared_task
def celery_demo_task3(param_dict):
    logger.info('foot task start! param_dict:%s' % param_dict)
    time.sleep(5)
    return 'finished'


def do_work(user):
    dispatch(celery_demo_task, {'x': user})
    dispatch(celery_demo_task3, {'z': user})
    sub_work(user)


def sub_work(user):
    dispatch(celery_demo_task2, {'y': user})


# 分发任务
def dispatch(task, param_dict):
    param_json = json.dumps(param_dict)

    try:
        task.apply_async(
            [param_json],
            retry=True,
            retry_policy={
                'max_retries': 1,
                'interval_start': 0,
                'interval_step': 0.2,
                'interval_max': 0.2,
            },
        )
    except Exception as ex:
        logger.info(ex)
        raise
