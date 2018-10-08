import json
import logging

from django.test import TestCase

log = logging.getLogger(__name__)


class Foo:
    def __init__(self, code):
        self.code = code


def foo2dict(obj):
    return {
        "code": obj.code,
        "msg": obj.msg
    }


def dict2foo(dict):
    obj = Foo(dict['code'])
    obj.msg = dict['msg']
    return obj


class JsonTest(TestCase):
    def test_obj_2_json(self):
        obj = Foo(1)
        obj.msg = 'msg'

        # obj to json
        obj_str = json.dumps(obj, default=foo2dict)
        log.info('str from obj: %s, %s' % (type(obj_str), obj_str))

        # json to obj
        obj_parse = json.loads(obj_str, object_hook=dict2foo)
        log.info('obj from str: %s, %s' % (type(obj_parse), obj_parse))
        self.assertEqual(obj.msg, obj_parse.msg)
        self.assertEqual(obj.code, obj_parse.code)

    def test_obj_2_dict(self):
        obj = Foo(1)
        obj.msg = 'msg'

        # obj to json
        obj_str = json.dumps(obj, default=foo2dict)
        log.info('str from obj: %s, %s' % (type(obj_str), obj_str))

        # obj to dict
        obj_dict = json.loads(obj_str)
        log.info('dict from str: %s, %s' % (type(obj_dict), obj_dict))
        self.assertDictEqual(foo2dict(obj), obj_dict)
