from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

from app.forms import RegisternForms
from django.contrib.auth.models import User
from app.models import Parameters

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html', context = {})

class ArticleDetailView(DetailView):

    model = Parameters
    template_name = 'dashboard/index.html'
    context_object_name = 'params'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def RegisterView(request):
    if request.method == 'POST':
        form = RegisternForms(request.POST)
        if form.is_valid():
            user = form.save()
            params = Parameters(user = user)
            params.save()
        
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

  
    
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(username, { "type": "update.params", "text": {'Hiep' : 'CP'},})
    
    

    return Response(status.HTTP_200_OK)
    

