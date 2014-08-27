from django.shortcuts import render_to_response
from django.http import HttpResponse
from process.forms import ProcessForm
from django.template import RequestContext
from process.models import Activity
import string
import random
import numpy
import math
import os
import binascii
import base64
import threading
import cv2
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process(request):
   
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        form = ProcessForm(data=request.POST)
        #form.x = int(request.POST['x'])
        if form.is_valid():
            userid = request.POST['userid']
            if not Activity.objects.filter(userid=userid).exists():
                print "does not exists"
                form.save()
            current_data = Activity.objects.get(userid=userid)
            x = request.POST["x"]
            y = request.POST["y"]
            z = request.POST["z"]
            current_data.x+=(","+x)
            print current_data.x
            current_data.y+=(","+y)
            current_data.z+=(","+z)
            xdata = current_data.x.split(",")
            ydata = current_data.y.split(",")
            zdata = current_data.z.split(",")
            count = len(xdata)
            dataBuffer = 10
            print xdata
            if count >= dataBuffer:

                xdata = map(float, xdata)
                ydata = map(float, ydata)
                zdata = map(float, zdata)
                
                xdata = xdata[len(xdata)-dataBuffer: len(xdata)]
                ydata = ydata[len(ydata)-dataBuffer: len(ydata)]
                zdata = zdata[len(zdata)-dataBuffer: len(zdata)]
               
                xsum = sum(xdata)
                ysum = sum(ydata)
                zsum = sum(zdata)
            
                xaverage = xsum/len(xdata)
                yaverage = ysum/len(ydata)
                zaverage = zsum/len(zdata)

                xSTD = numpy.std(xdata)
                ySTD = numpy.std(ydata)
                zSTD = numpy.std(zdata)

                averageResultant = 0
                xAveAbsDiff=0
                yAveAbsDiff=0
                zAveAbsDiff=0

                for i in range (0,len(xdata)):
                    xAveAbsDiff = xAveAbsDiff +math.fabs(xdata[i]-xaverage)
                    yAveAbsDiff = yAveAbsDiff +math.fabs(ydata[i]-yaverage)
                    zAveAbsDiff = zAveAbsDiff +math.fabs(zdata[i]-zaverage)
                    averageResultant = averageResultant+math.sqrt(math.pow(xdata[i],2)+math.pow(ydata[i],2)+math.pow(zdata[i],2))
                averageResultant= averageResultant/len(xdata)
                xAveAbsDiff=xAveAbsDiff/len(xdata)
                yAveAbsDiff=yAveAbsDiff/len(ydata)
                zAveAbsDiff=zAveAbsDiff/len(zdata)

                data = numpy.ndarray((1,10))
                data[:,0]=xaverage
                data[:,1]=yaverage
                data[:,2]=zaverage
                data[:,3]=xSTD
                data[:,4]=ySTD
                data[:,5]=zSTD
                data[:,6]=xAveAbsDiff
                data[:,7]=yAveAbsDiff
                data[:,8]=zAveAbsDiff
                data[:,9]=averageResultant
                data = data.astype(numpy.float32)
                previous = numpy.load(('/Users/niajafarve/Development/moveyourglass/traindata.npz'))
                alldata = previous['alldata']
                labels = previous['labels']

                knn = cv2.KNearest()
                #print alldata.shape
                #print labels.shape
                knn.train(alldata,labels)
                ret,result,neighbours,dist = knn.find_nearest(data,k=3)
                #print result[0][0]
                guess = result[0][0]
                if guess == 0.0:
                    current_data.currentTotal+="0,"
                    current_data.save()
                    return render_to_response('result.html',{'result': "sitting"},context_instance=RequestContext(request))
                elif guess ==1.0:
                    current_data.currentTotal+="1,"
                    current_data.save()
                    return render_to_response('result.html',{'result': "walking"},context_instance=RequestContext(request))
                else:
                    current_data.currentTotal+="2,"
                    current_data.save()
                    return render_to_response('result.html',{'result': "running"},context_instance=RequestContext(request))
            else:
                current_data.save()
                return HttpResponse("Not enough data")
        else:
            print form.errors

    
    else:
        form = ProcessForm()

    # Render the template depending on the context.
    return render_to_response(
            'process.html',
            {'form': form},
            context_instance=RequestContext(request)
            )

def summary(request, userid):
    userData = Activity.objects.get(userid=userid)
    totals = userData.currentTotal
    totals = totals.split(',')
    print totals
    walkingTotal = 0
    sittingTotal = 0
    runningTotal = 0
    for i in range(totals):
        if totals[i]==0:
            sittingTotal+=1
        elif totals[i]==1:
            walkingTotal +=1
        elif totals[i]==2:
            runningTotal+=1
    return render_to_response('summary.html',
        {'walking':walkingTotal, 'sitting':sittingTotal, 'running':runningTotal},
        context_instance=RequestContext(request)
        )


