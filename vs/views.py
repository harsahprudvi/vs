from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import CreateView
from .models import Candidate, Position,ControlVote
from .forms import RegistrationForm,LoginForm

def indexview(request):
    return render(request,'index.html')


def detailview(request):
    return render(request,'detail.html')


def loginView(request):
    context={}
    if request.user.is_authenticated:
        return redirect('vs:poll')
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('vs:poll')
    else:
        form=LoginForm()
    context['logform']=form
    return render(request,'login.html',context)


def logoutview(request):
    logout(request)
    return redirect('/')


@login_required(login_url="vs:login")
def pollview(request):
    obj = Position.objects.all()
    return render(request, 'poll.html',{'obj':obj})

def registrationview(request):
    context={}
    if request.user.is_authenticated:
        return redirect('vs:poll')
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vs:login')
        else:
            context['regform']=form
    else:
        form=RegistrationForm()
        context['regform']=form
    return render(request,'register.html',context)
    
def logoutView(request):
    logout(request)
    return redirect('vs:index')

@login_required
def resultView(request):
    obj = Candidate.objects.all().order_by('position','-total_vote')
    return render(request, "result.html", {'obj':obj})


@login_required
def candidateView(request, pos):
    obj = get_object_or_404(Position, pk = pos)
    if request.method == "POST":
        temp = ControlVote.objects.get_or_create(user=request.user, position=obj)[0]
        if temp.status == False:
            temp2 = Candidate.objects.get(pk=request.POST.get(obj.title))
            temp2.total_vote += 1
            temp2.save()
            temp.status = True
            temp.save()
            return HttpResponseRedirect('/poll/')
        else:
            messages.success(request, 'you have already been voted this position.')
            return render(request, 'candidate.html', {'obj':obj})
    else:
        return render(request, 'candidate.html', {'obj':obj})

@login_required
def candidateDetailView(request, id):
    obj = get_object_or_404(Candidate, pk=id)
    return render(request, "candidate_detail.html", {'obj':obj})