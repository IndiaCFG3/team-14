from django.shortcuts import render
from django.http import request, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.




@csrf_exempt
def webhook(request):

    if request.method == "POST":

        res = json.loads(request.body)
        print(res.get('queryResult'))
        response = {
            'fulfillmentText': "Slot Booked.Do u have anu further queries?"}

        return JsonResponse(response)



