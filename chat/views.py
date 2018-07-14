from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from django.shortcuts import render
from.models import *
from chat.models import Chat


# Create your views here.





def getmessage(request):
    chat_1=Chat.objects.all()
    #print(chat_1)
    ref=request.user
    #print(ref)

    a=[]
    mychat=[]
    #
    for r in chat_1:
        if r.sender.username == request.user.username or r.receiver.username == request.user.username:
            mychat.append(r)
    print(mychat)
    for chat in mychat:
        #print(chat.sender.username)
        #print(chat.receiver.username)
        if chat.sender.username != request.user.username:
            if chat.sender.username not in a:
                a.append(chat.sender.username)
        if chat.receiver.username != request.user.username:
            if chat.receiver.username not in a:
                a.append(chat.receiver.username)
    return render(request,'alpha/getmessage.html',{'result':a})







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
    receiver = "nirajan"
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


        receiver = username


        if msg != '':
            s1 = User.objects.get(username=sender)
            r1 = User.objects.get(username=receiver)
            c = Chat(message=msg,sender=s1,receiver=r1)
            c.save()


        return JsonResponse({'msg': msg})
    else:
        return HttpResponse('Request must be POST.')


def Messages(request,username):
    def AND(a, b):
        return (a and b)
    def equal(a,b):
        if a == b:
            return True
        else:
            return False
    c = Chat.objects.all()
    sender = request.user
    receiver = username
    s1 = User.objects.get(username=sender)
    r1 = User.objects.get(username=receiver)
    a = list()
    for obj in c:
        if AND(equal(obj.sender, s1), equal(obj.receiver, r1)) or AND(equal(obj.sender, r1), equal(obj.receiver, s1)):
            a.append(obj)
    return render(request, 'alpha/messages.html', {'chat': a,'r1':r1,'s1':s1})
