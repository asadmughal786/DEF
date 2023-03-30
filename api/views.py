from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt
from .serializers import StudentsSerializer



# Create your views here.

@csrf_exempt
def studentAPI(request):
    if request.method == "GET":
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentsSerializer(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentsSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == "POST":
        json_data =request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentsSerializer(data=python_data)
        print('----------------> working')
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method =='PUT':
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id) 
        serializer = StudentsSerializer(stu,data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Updated!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type = 'application/json')

    if request.method == 'DELETE':
        json_data = request.body 
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg':'data deleted!'}
        # json_data= JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)

        


