import json
import logging

from django.test import TestCase

log = logging.getLogger(__name__)


class Foo:
    def __init__(self, code):
        self.code = code
        self.msg = None


class FooEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Foo):
            return foo2dict(o)

        super(FooEncoder, self).default(o)


def foo2dict(obj):
    return {
        "code": obj.code,
        "msg": obj.msg
    }


def dict2foo(dict_parse):
    obj = Foo(dict_parse['code'])
    obj.msg = dict_parse['msg']
    log.info(dict_parse.get('unknown_field'))
    return obj


class JsonTest(TestCase):
    def test_list_2_json(self):
        obj_list = [Foo(1), Foo(2)]
        obj_list[0].msg = 'msg0'
        obj_list[1].msg = 'msg1'

        # obj list to json
        obj_str = json.dumps(obj_list, cls=FooEncoder)
        log.info('str from obj: %s, %s' % (type(obj_str), obj_str))

        # json to obj
        obj_parse = json.loads(obj_str, object_hook=dict2foo)
        log.info('obj from str: %s, %s' % (type(obj_parse), obj_parse))

        for i, obj in enumerate(obj_list):
            self.assertTrue(isinstance(obj_parse[i], Foo))
            self.assertEqual(obj.msg, obj_parse[i].msg)
            self.assertEqual(obj.code, obj_parse[i].code)

    def test_obj_2_json(self):
        obj = Foo(1)
        obj.msg = 'msg'

        # obj to json
        obj_str = json.dumps(obj, default=foo2dict)
        log.info('str from obj: %s, %s' % (type(obj_str), obj_str))

        # json to obj
        obj_parse = json.loads(obj_str, object_hook=dict2foo)
        log.info('obj from str: %s, %s' % (type(obj_parse), obj_parse))
        self.assertTrue(isinstance(obj_parse, Foo))

        self.assertEqual(obj.msg, obj_parse.msg)
        self.assertEqual(obj.code, obj_parse.code)

    def test_obj_2_dict(self):
        obj = Foo(2)
        obj.msg = 'msg'

        # obj to json
        obj_str = json.dumps(obj, default=foo2dict)
        log.info('str from obj: %s, %s' % (type(obj_str), obj_str))

        # obj to dict
        obj_dict = json.loads(obj_str)
        log.info('dict from str: %s, %s' % (type(obj_dict), obj_dict))
        self.assertDictEqual(foo2dict(obj), obj_dict)
