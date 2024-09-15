from django.shortcuts import render,HttpResponse
from main.models import Record
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

record = Record.objects.values('Academic_Program_Name').distinct()
Round = Record.objects.values('Round').distinct()

# Create your views here.
def index(request):
        return render(request,'index.html',{'courses':record,'rounds':Round})

@csrf_exempt
def predicator_view(request):
        if request.method == "POST":
            rank = int(request.POST['rank'])
            cate = request.POST['category']
            gender = request.POST['gender']
            iit = request.POST['iit']
            courses = request.POST['courses']
            rounds = request.POST['round']
            if request.POST['iit'] == 'all':
                if request.POST['courses'] == 'all':
                        result = Record.objects.filter(Closing_Rank__gt=rank, Seat_Type__icontains=cate,Gender__icontains=gender,Round__icontains=rounds,Year='2022').order_by('Closing_Rank').values()
                        if request.POST['rank'] == '1':
                                result = Record.objects.filter(Seat_Type__icontains=cate,Gender__icontains=gender,Round__icontains=rounds,Year='2022').order_by('Closing_Rank').values()
                else:
                        result = Record.objects.filter(Closing_Rank__gt=rank, Seat_Type__icontains=cate,Gender__icontains=gender,Academic_Program_Name__icontains=courses,Round__icontains=rounds,Year='2022').order_by('Closing_Rank').values()
            else:
                result = Record.objects.filter(Closing_Rank__gt=rank, Seat_Type__icontains=cate,Gender__icontains=gender,Institute__icontains=iit,Academic_Program_Name__icontains=courses,Round__icontains=rounds,Year='2022').order_by('Closing_Rank').values()
            return render(request,'predicator.html',{'data':result})
        return render(request,'predicator.html')
# def predicator_view(request):
#         if request.method == "POST":
#             rank = int(request.POST['rank'])
#             cate = request.POST['category']
#             gender = request.POST['gender']
#             iit = request.POST['iit']
#             courses = request.POST['courses']
#             rounds = request.POST['round']
#             if request.POST['iit'] == 'all':
#                 if request.POST['courses'] == 'all':
#                         result = Record.objects.filter(Closing_Rank__lte=rank, Seat_Type__icontains=cate,Gender__icontains=gender,Round__icontains=rounds).values()
#                 else:
#                         result = Record.objects.filter(Closing_Rank__lte=rank, Seat_Type__icontains=cate,Gender__icontains=gender,Academic_Program_Name__icontains=courses,Round__icontains=rounds).values()
#             else:
#                 result = Record.objects.filter(Closing_Rank__lte=rank, Seat_Type__icontains=cate,Gender__icontains=gender,Institute__icontains=iit,Academic_Program_Name__icontains=courses,Round__icontains=rounds).values()
#             responses = result.values('Year','Opening_Rank').distinct()
#             x = []
#             y = []
#             fig, ax = plt.subplots()
#             for response in responses:
#                 x.append(response["Year"])
#                 y.append(response["Opening_Rank"])
#             ax.plot(x, y)
#             tick_interval = 150
#             ax.yaxis.set_major_locator(plt.MultipleLocator(tick_interval))
#             plt.xticks(rotation=90)
#             buffer = io.BytesIO()
#             plt.savefig(buffer, format='png')
#             buffer.seek(0)
#             image_base64 = base64.b64encode(buffer.getvalue()).decode()
#             return render(request,'index.html',{'base64':image_base64,'courses':record,'rounds':Round})
#         return render(request,'index.html',{'courses':record,'rounds':Round})


def analyse_iit_view(request):
    record = Record.objects.values('Institute').distinct()
    # r = Record.objects.values('Academic_Program_Name').distinct()
    # values_list = [item['Institute'] for item in record]
    # values_str = ''.join(values_list)
    return render(request,'analyse.html',{'record':record})

def analyse_branch_view(request):
    record = Record.objects.values('Academic_Program_Name').distinct()
    return render(request,'list_branches.html',{'record':record})

def analyse_branch_cut_view(request):
        record = Record.objects.values('Academic_Program_Name','Round','Year','Closing_Rank','Opening_Rank').distinct()[:100:1]
        ops = Record.objects.values('Academic_Program_Name').distinct()
        op = Record.objects.values('Round').distinct()
        if request.method == "POST":
                cate = request.POST['category']
                gender = request.POST['gender']
                iit = request.POST['iit']
                courses = request.POST['courses']
                rounds = request.POST['round']
                result = Record.objects.filter(Seat_Type__icontains=cate,Gender__icontains=gender,Institute__icontains=iit,Academic_Program_Name__icontains=courses,Round__icontains=rounds).values()
                responses = result.values('Year','Opening_Rank').distinct()
                x = []
                y = []
                for response in responses:
                        x.append(response["Year"])
                        y.append(response["Opening_Rank"])
                plt.plot(x, y)
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.getvalue()).decode()
                return render(request,'analyse_branch1.html',{'ops':ops,'op':op,'base64':image_base64})
        return render(request,'analyse_branch1.html',{'record':record,'ops':ops,'op':op})


@csrf_exempt
def analyse_inst_cut_view(request):
        record = Record.objects.values('Institute','Round','Closing_Rank','Opening_Rank','Year').distinct()[:100:1]
        ops = Record.objects.values('Academic_Program_Name').distinct()
        op = Record.objects.values('Round').distinct()
        if request.method == "POST":
                cate = request.POST['category']
                gender = request.POST['gender']
                iit = request.POST['iit']
                courses = request.POST['courses']
                rounds = request.POST['round']
                result = Record.objects.filter(Seat_Type__icontains=cate,Gender__icontains=gender,Institute__icontains=iit,Academic_Program_Name__icontains=courses,Round__icontains=rounds).values().distinct()
                responses = result.values('Year','Opening_Rank').distinct()
                x = []
                y = []
                for response in responses:
                        x.append(response["Year"])
                        y.append(response["Opening_Rank"])
                plt.plot(x, y)
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png')
                buffer.seek(0)
                image_base64 = base64.b64encode(buffer.getvalue()).decode()
                return render(request,'analyse_institute1.html',{'ops':ops,'op':op,'base64':image_base64})
        return render(request,'analyse_institute1.html',{'record':record,'ops':ops,'op':op})

def iitwise_view(request,inst):
    fec= Record.objects.filter(Institute=inst).values('Academic_Program_Name').distinct()
    uit= Record.objects.filter(Institute=inst).values('Year').distinct()
    return render(request,'iitwise.html',{'daa': fec,'uit':uit})

def coursewise_view(request,inst):
    fec= Record.objects.filter(Academic_Program_Name=inst).values('Institute','Academic_Program_Name').distinct()
    uit= Record.objects.filter(Academic_Program_Name=inst).values('Academic_Program_Name','Year').distinct()
    return render(request,'coursewise.html',{'das': fec,'uit':uit})