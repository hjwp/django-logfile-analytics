from django.shortcuts import render
from analytics.models import Hit

def home(request):
    return render(request, 'home.html',
            {'hits': Hit.objects.all()}
    )
