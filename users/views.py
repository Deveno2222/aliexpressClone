from django.shortcuts import render

# Create your views here.
def index(request):
  context = {
    'name': 'Dias',
    'age': 19,
  }
  return render(request, 'myapp/index.html', context)