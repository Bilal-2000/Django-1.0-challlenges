from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges_dict = {
    "january" : "This is january",
    "febrary" : "This is febrary",
    "march" : "This is march",
    "april" : "This is april",
    "may" : "This is may",
    "june" : "This is june",
    "july" : "This is july",
    "august" : "This is august",
    "september" : "This is sep",
    "october" : "This is october",
    "november" : "This is november",
    "december":None
}

number={
    1:"january",
    2:"febrary",
    3:"march",
    4:"april",
    5:"may",
    6:"june",
    7:"july",
    8:"august",
    9:"september",
    10:"october",
    11:"november",
    12:"december"
}

def index(request):
    months = monthly_challenges_dict.keys()
    return render(request,"challenges/index.html",{"months" : months})

def monthly_challenges_a_number(request,month):
    try:
        challenge_text = number[month]
        redirect_path = reverse("only-url",args=[challenge_text])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound(month)


def monthly_challenges(request,month):
    try:
        challenge_text = monthly_challenges_dict[month] 
        return render(request,"challenges/challenge.html",{"text" :challenge_text,"mon": month,"challenge":"Challenge"})
    except:
        response_text = render_to_string("404.html")
        return HttpResponseNotFound(response_text)
    