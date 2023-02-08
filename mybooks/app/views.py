from django.shortcuts import render

# Create your views here.
def indexView(request):
    template = 'index.html'
    return render(request, template)