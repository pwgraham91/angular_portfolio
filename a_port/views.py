from django.shortcuts import render

# Create your views here.
def index(request):
    data = {'logged_user': request.user}
    return render(request, "index.html", data)