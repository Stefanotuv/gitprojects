from django.shortcuts import render, render_to_response
from django.template import Context, loader

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
