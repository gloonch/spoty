from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Spot
from django.http import JsonResponse
import uuid


# Create your views here.
@csrf_exempt
def sign_up(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    pass1 = request.POST.get('password')
    pass2 = request.POST.get('password_repeat')

    if name == "" and email == "" and pass1 == "" and pass2 == "":
        return JsonResponse({
            'status': 400,
        })
    if not pass2 == pass1:
        return JsonResponse({
            'status': 500,
            'result': 'Passwords are not the same'
        })
    else:
        # checks again if phone_number does not exits then try ...
        if User.objects.filter(email=email).exists() == False:
            try:
                generated_token = uuid.uuid1().hex
                user = User(name=name,
                            email=email,
                            password=pass1,
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


@csrf_exempt
def sign_in(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == "" and password == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        try:
            user = User.objects.get(email=email)
            if password == user.password:
                return JsonResponse({
                    'status', 200,
                })
            if not password == user.password:
                return JsonResponse({
                    'status', 404,
                })
        except Exception as err:
            return JsonResponse(
                {'status': 500,
                 'error': err.__str__(),
                 },
                safe=False
            )


@csrf_exempt
def add_spot(request):
    user = request.POST.get('user')
    lat = request.POST.get('latitude')
    lon = request.POST.get('longitude')
    desc = request.POST.get('description')

    if user == "" and lat == "" and \
            lon == "" and desc == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        try:
            user_id = User.objects.get(pk=user)
            s = Spot.objects.create(latitude=lat, longitude=lon,
                                    description=desc, user=user_id)
            return JsonResponse({'result': 200}, )
        except Exception as err:
            return JsonResponse({
                'result': 500,
                'error': err.__str__(),
            })


@csrf_exempt
def delete_spot(request):
    spot_id = request.POST.get('id')
    if spot_id == "":
        return JsonResponse({
            'status': 400,
        })
    else:
        try:
            Spot.objects.filter(pk=spot_id).delete()
            return JsonResponse({
                'status': 200,
            })
        except Exception as error:
            return JsonResponse({
                'status': 500,
                'result': error.__str__(),
            })
