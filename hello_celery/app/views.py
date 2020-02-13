from django.http import JsonResponse

from hello_celery.tasks import do_task


def chk_job(req):
    param_dict = {
        'url': req.get_raw_uri(),
        'path': req.get_full_path(),
        'host': req.get_host(),
    }
    job = do_task(param_dict)
    return JsonResponse({'code': 0, 'msg': 'success', 'job': job.task_id})
