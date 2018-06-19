from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def Home(request):
    return render(request, 'mentor/home.html')

# Create your views here.
