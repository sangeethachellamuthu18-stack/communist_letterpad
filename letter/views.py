
# Create your views here.
from django.shortcuts import render

def home(request):
    content = ""

    if request.method == "POST":
        content = request.POST.get("content")

    return render(request, "letter.html", {"content": content})