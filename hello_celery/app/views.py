import traceback

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .tasks import do_work


@csrf_exempt
def chk_celery(request):
    if request.method == 'GET':
        try:
            user = request.GET.get('username')
            do_work(user)
            return JsonResponse({'code': 0, 'msg': 'success'})
        except:
            return JsonResponse({'code': -1, 'msg': traceback.format_exc()})
