from django.shortcuts import render, render_to_response
from django.template import Context, loader
from exercise.models import AppUser

# Create your views here.

from django.http import HttpResponse


def index(request):
    testDict = {'testfromexercise':'TEST FROM INDEX'}
    return render(request, 'exercise/index.html',context=testDict)


def exercise(request):
    # all the options below work. the diffence in the path would require to
    # declare the different referetn DIR in settings-> TEMPLATES /> DIR
    # return render(request, 'exercise/exercise.html')
    # return render(request, 'exercise.html') - required BASE_DIR+'/exercise'
    # return render_to_response('exercise/exercise.html')
    # return render_to_response('exercise.html') - required BASE_DIR+'/exercise'
    # template = loader.get_template("exercise/exercise.html")
    #
    # return HttpResponse(template.render())
    # return HttpResponse("Exercise page from HttpResponse")
    testDict = {'testfromexercise':'TEST FROM EXERCISE'}
    return render(request, 'exercise/exercise.html',context=testDict)

def users(request):

    user_list = AppUser.objects.order_by('surname')
    user_dict = {"users":user_list}
    return render(request,'exercise/users.html',context=user_dict)

def usersNew(request):

    user_list = AppUser.objects.order_by('name')
    j=0
    numbers = []
    for i in user_list:
        numbers.append(j)
        j=j+1

    user_dict = {"users":user_list,"numbers":numbers}
    return render(request,'exercise/usersNew.html',context=user_dict)
