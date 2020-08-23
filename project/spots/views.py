from django.shortcuts import render
from .models import User
from django.http import JsonResponse
import uuid


# Create your views here.
def add_user(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    if name == "" and email == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        # checks again if phone_number does not exits then try ...
        if User.objects.filter(email=email).exists() == False:
            try:
                generated_token = uuid.uuid1().hex
                user = User(name=name,
                            email=email,
                            token=generated_token)
                user.save()
                return JsonResponse(
                    {'token': generated_token,
                     'status': 200, }
                )
            except Exception as error:
                return JsonResponse(
                    {'status': 500,
                     'error': error.__str__(), }
                )
        else:
            JsonResponse({
                'result': 'email exists',
            })

    return JsonResponse({
        'status': 400,
    })


def add_spot(request):
    user = request.POST.get('user')
    lat = request.POST.get('lat')
    lon = request.POST.get('lon')
    desc = request.POST.get('desc')

    pass
