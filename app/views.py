from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

from app.forms import RegisternForms
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

def RegisterView(request):
    if request.method == 'POST':
        form = RegisternForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = RegisternForms()
    
    return render(request, 'registration/register.html', context = {'form': form})

@api_view(['PUT'])
def update_params(request, username):
    """
    Update parameters
    :username username of an user
    :return status code
    """
    try:
        user = User.objects.get(username = username)
    except:
        return Response(status.HTTP_401_UNAUTHORIZED)

    if not user.check_password(request.data['password']):
        return Response(status.HTTP_401_UNAUTHORIZED)

    
    
    

    return Response(status.HTTP_200_OK)
    

