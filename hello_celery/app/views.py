import traceback

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .tasks import do_job


@csrf_exempt
def chk_celery(request):
    if request.method == 'GET':
        try:
            user = request.GET.get('username')
            job = do_job(user)
            return JsonResponse({'code': 0, 'msg': 'success', 'job': job.task_id})
        except:
            return JsonResponse({'code': -1, 'msg': traceback.format_exc()})
