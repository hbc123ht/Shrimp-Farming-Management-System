from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from app.forms import RegisternForms
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

