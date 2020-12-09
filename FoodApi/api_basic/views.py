from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Food
from .serializers import FoodSerializer


# Create your views here.
@csrf_exempt
def FoodList(request):

    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FoodSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def food_detail(request, name):
    try:
        food = Food.objects.get(pk=name)

    except Food.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serilizer = FoodSerializer(food)
        return  JsonResponse(serilizer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FoodSerializer(food, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        food.delete()
        return HttpResponse(status=204)



