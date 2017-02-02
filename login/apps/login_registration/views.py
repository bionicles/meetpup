from django.shortcuts import render, HttpResponse, redirect
from models import User, Event
from django.contrib import messages
from django.urls import reverse

# Create your views here.


def index(request):

    return render(request, "login_registration/index.html")

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request,messages.INFO, message)

def loginvalidate(request):
    if request.method == "POST":
        print 'here'
        print request.POST['email']
        result = User.objects.loginvalidation(request.POST)
        print "Login validation complete"
        # print result

        if result[0] == False:
            print_messages(request, result[1])
            return redirect(reverse('index'))
        # print request
        print result[1]
        print "Passing to the login function"
        return login(request, result[1])
    else:
        print "Method's not even post for loginvalidate"
        return redirect('/')

def login(request, user):
    print "Here at Login"
    request.session['user'] = {
    'id': user.id,
    'firstname' : user.firstname,
    'lastname' : user.lastname,
    'email' : user.email,
    'zip':user.zipcode,
    }
    return redirect('success')

def registervalidate(request):
    result= User.objects.registervalidation(request.POST)

    if not result[0]:
        print_messages(request, result[1])
        return redirect('register')

    return login(request, result[1])


def success(request):
    if not 'user' in request.session:
        return redirect('/')
    request.session['zip']='37.386402,-121.925215'
    print request.session['zip']
    return render(request, 'login_registration/success.html')
def zipupdate(request):
    return redirect('success')

def eventform(request):

    return render(request,'login_registration/eventform.html')
def createevent(request):
    user=request.session['user']['id']
    print user
    result= Event.objects.eventcreator(request)

    return redirect('community')

def logout(request):
    request.session.clear()
    # request.session.pop('user')
    return redirect('/')

def register(request):
    return render(request, 'login_registration/registration.html')

def community(request):
    return render(request, 'login_registration/community.html')

def adoption(request):
    return render(request, 'login_registration/adoption.html')
