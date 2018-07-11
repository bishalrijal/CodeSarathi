from django.shortcuts import render

# Create your views here.
from django.shortcuts import render ,reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat
from CodeSarathi import settings
# Create your views here.
def index(request):
# return render_to_response('index.html')
    return render(request, 'alpha/login.html', {'next': next})


# def Login(request):
#     next = request.GET.get('next', '/home/')
#     if request.method == "POST":
#
#         username = request.POST['username']
#         password = request.POST['password']
#         request.session['receiver'] = request.POST['username2']
#         print(request.session['receiver'])
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 #WelcomeUser(user)
#                 return HttpResponseRedirect(next)
#             else:
#                 return HttpResponse("Account is not active at the moment.")
#         else:
#             return HttpResponseRedirect(settings.LOGIN_URL)
#     return render(request, "alpha/login.html", {'next': next})

def Logout(request):
    # logout(request)
    Chat.objects.all().delete()
    return HttpResponseRedirect('/login/')


def Home(request,username):
    # request.session['receiver'] = username

    def AND(a, b):
        return (a and b)
    def equal(a,b):
        if a == b:
            return True
        else:
            return False
    print(username)
    sender = request.user
    c = Chat.objects.all()
    # receiver = request.session['receiver']
    receiver = username
    s1 = User.objects.get(username=sender)
    r1 = User.objects.get(username=receiver)
    a=list()
    for obj in c:
        if AND(equal(obj.sender,s1),equal(obj.receiver,r1)) or AND(equal(obj.sender,r1),equal(obj.receiver,s1)):
            a.append(obj)
    return render(request, "alpha/home.html", {'home': 'active', 'chat': a,'r1':r1,'s1':s1})


def Post(request,username):

    if request.method == "POST":
        sender = request.user
        msg = request.POST.get('msgbox', None)
        print(msg)
        print()
        receiver = request.session['receiver']


        if msg != '':
            s1 = User.objects.get(username=sender)
            r1 = User.objects.get(username=receiver)
            c = Chat(message=msg,sender=s1,receiver=r1)
            c.save()


        return JsonResponse({'msg': msg})
    else:
        return HttpResponse('Request must be POST.')


def Messages(request):
    def AND(a, b):
        return (a and b)
    def equal(a,b):
        if a == b:
            return True
        else:
            return False
    c = Chat.objects.all()
    sender = request.user
    receiver = request.session['receiver']
    s1 = User.objects.get(username=sender)
    r1 = User.objects.get(username=receiver)
    a = list()
    for obj in c:
        if AND(equal(obj.sender, s1), equal(obj.receiver, r1)) or AND(equal(obj.sender, r1), equal(obj.receiver, s1)):
            a.append(obj)
    return render(request, 'alpha/messages.html', {'chat': a,'r1':r1,'s1':s1})
