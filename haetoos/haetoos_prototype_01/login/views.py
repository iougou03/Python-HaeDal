from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# from django.contrib.auth import authenticate

from .models import Haetoos_member

# Create your views here.
def index(request):
    return render(request,'login/index.html')

def sign_in(request):
    if request.method == 'POST':
        try: 
            person = Haetoos_member.objects.get(haetoos_id =request.POST['haetoos_id'])
            if person.haetoos_ps ==request.POST['haetoos_ps']:
                message = 'logined Succesfully!'
            else:
                message = 'wrong password'
        except Haetoos_member.DoesNotExist:
            message = 'ID doesn\'t exist.'

        return render(request,'login/result.html',{'message':message})

    elif request.method == 'GET':
        return render(request,'login/sign_in.html')

def sign_up(request) :
    return render(request,'login/sign_up.html')

def result(request) :
    name = request.POST['name'] #문자열 반환
    student_id = request.POST['student_id']

    try:
        person = Haetoos_member.objects.get(student_id = student_id) #해당하는 row를 반환
    except Haetoos_member.DoesNotExist: #미등록된 사용자
        message = 'Failed to Create. Ask manager to join the club'

    if person.name==name: #등록된 사용자일 경우
        person.haetoos_id = request.POST['haetoos_id']
        person.haetoos_ps = request.POST['haetoos_ps']
        person.save()

        message ='Create Succesfully!'
    
    return render(request,'login/result.html',{'message':message})


    