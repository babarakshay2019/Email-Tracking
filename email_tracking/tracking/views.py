from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


@csrf_exempt
def eventAPI(request):
    import pdb
    pdb.set_trace()
    return JsonResponse({"is_payment_pending": True})
