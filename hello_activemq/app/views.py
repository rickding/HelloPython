import json

from django.http import HttpResponse

from hello_activemq.service import mq_service as mq


def chk_mq(req):
    msg = json.dumps({
        'url': req.get_raw_uri(),
        'path': req.get_full_path(),
        'host': req.get_host(),
    })
    mq.send_msg_to_queue(msg)

    return HttpResponse(msg)
