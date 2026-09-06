from django.shortcuts import render

# Create your views here.
def blogRoot(request):
    return render(request, 'blogRoot.html')