import json

from django.http import HttpResponse

from hello_activemq.mq import mq_service as mq


def chk_mq(req):
    msg_dict = {
        'url': req.get_raw_uri(),
        'path': req.get_full_path(),
        'host': req.get_host(),
    }

    mq.send_msg_to_queue(msg_dict)
    mq.send_msg_to_topic(msg_dict)

    return HttpResponse(json.dumps(msg_dict))
