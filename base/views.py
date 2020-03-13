from django.shortcuts import render
from .models import User, Spot
from django.http import JsonResponse
import uuid


# Create your views here.

# first check if user's email exists
def is_email_registered(request):
    email = request.GET.get('email')
    if email == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        if User.objects.filter(email=email).exists():
            return JsonResponse({
                'isRegistered': True, })
        else:
            return JsonResponse({
                'isRegistered': False, })


# gets email and nickanme and registers the user
def generate_token(request):
    nickname = request.GET.get('nickname')
    email = request.GET.get('email')
    if nickname == "" and email == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        # checks again if phone_number does not exits then try ...
        if User.objects.filter(email=email).exists() == False:
            try:
                generated_token = uuid.uuid1().hex
                user = User(nickname=nickname,
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
