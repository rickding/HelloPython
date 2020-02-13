from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from hello_celery.tasks import do_task


@csrf_exempt
def chk_celery(request):
    if request.method == 'GET':
        user = request.GET.get('username')
        job = do_task({'x': user})
        return JsonResponse({'code': 0, 'msg': 'success', 'job': job.task_id})
