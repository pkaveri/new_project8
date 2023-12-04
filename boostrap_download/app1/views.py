from django.shortcuts import render

# Create your views here.
def boostrap(request):
    return render(request,'boostrap.html')