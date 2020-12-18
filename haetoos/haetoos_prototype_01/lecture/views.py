from django.shortcuts import render,redirect

from .models import LectureList
# Create your views here.
def index(request):
    page = LectureList.objects.get(id=1)
    
    return render(request, 'lecture/index.html', {'content':page.content})