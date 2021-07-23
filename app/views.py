from django.http import request
from app.utils import CheckQuality, send_alert
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
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

@method_decorator(login_required, name='dispatch')
class Dashboard(TemplateView):

    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['param'] = Parameters.objects.get(user = self.request.user)
        return context


def RegisterView(request):
    if request.method == 'POST':
        form = RegisternForms(request.POST)
        if form.is_valid():
            user = form.save()
            params = Parameters.objects.create(user = user)
        
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

    data = request.data  

    user = User.objects.get(username = username)
    Parameters.objects.filter(user = user).update(
                                            ph = data['pH'],
                                            temp = data['temp'],
                                            salinity = data['salinity'],
                                            alkalinity = data['alkalinity'],
                                            oxygen = data['oxygen'],
                                            hydrogen_sulfide = data['hydrogen_sulfide'],
                                            amonia = data['amonia'],
                                            nitrit = data['nitrit'],     
                                            )
    # list of parameters to be checked
    params = ['temp', 'salinity', 'pH', 'alkalinity', 'oxygen', 'hydrogen_sulfide', 'amonia', 'nitrit']
    

    output = {}     # output for json data
    for param in params:
        output[param + '_value'] = data[param]
        output[param + '_notice'] = CheckQuality(param, data[param])
        if output[param + '_notice'] != 'The value is fine':
            send_alert()

 
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(username, { "type": "update.params", "text": output})
    
    

    return Response(status.HTTP_200_OK)
    

