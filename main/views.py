from django.shortcuts import render, HttpResponse, redirect
from random import randint

def index(request):
    if 'gold' in request.session:
        pass
    else:
        request.session['gold']=0
        request.session['log']=[]
    return render(request, "index.html")

def process(request):
    sum=int(request.session['gold'])
    clicked=request.POST['location']

    if clicked=="farm":
        amount=randint(10,20)
        sum+=amount
        string=f"Earned {amount} from the farm"
        request.session['log'].append(string)
    if clicked=="cave":
        amount=randint(5,10)
        sum+=amount
        string=f"Earned {amount} from the cave"
        request.session['log'].append(string)
    if clicked=="house":
        amount=randint(2,5)
        sum+=amount
        string=f"Earned {amount} from the house"
        request.session['log'].append(string)
    if clicked=="casino":
        amount=randint(10,50)
        sum+=amount
        string=f"Lost {amount} from the casino"
        request.session['log'].append(string)
    request.session['gold']=sum
    
    return redirect("/")


# Create your views here.
