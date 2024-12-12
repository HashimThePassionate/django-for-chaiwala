from django.shortcuts import render

# Create your views here.
def home(request):
    context = {  # new
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3",'Hi','Hello','Bye'],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, 'home.html', context)