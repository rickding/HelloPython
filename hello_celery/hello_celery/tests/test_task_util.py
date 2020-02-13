import logging

from django.test import TestCase

from hello_celery.tasks import task
from hello_celery.util.task_util import get_task_status

log = logging.getLogger(__name__)


class TasksTest(TestCase):
    def test_get_task_status(self):
        t = task.delay('test_task')
        ret = get_task_status(task, t.id)

        log.info('task status: %s,%s, %s' % (ret, t.id, str(task)))
        self.assertIsNotNone(ret.get('status'))
