from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse



# Create your views here.
days_dict={
    "monday":"hello monday",
    "tuesday":"hello tuesday",
    "wednesday":"hello wednesday",
    "thursday":"hello thursday",
    "friday":"hello friday",
    "sunday":"hello sunday",
    "saturday":"hello saturday",
}

def days_number(request,weeks):
    list_weeks=list(days_dict.values())
    if len(list_weeks) >=weeks:
        weekly=list_weeks[weeks-1]
        return HttpResponse(weekly)
        redireect_path=reverse("weekss",args=[weekly])
        return HttpResponseRedirect(redireect_path)
    else:
        return HttpResponseNotFound("weeks only contain 7 days")  

def days_string(request,weeks):
    list_weeks= days_dict[weeks]
    return HttpResponse(list_weeks) 

def get_templates(request,weeks):
    list_weeks=days_dict[weeks]
    return HttpResponse(f"<h1>{list_weeks}</h1>")    