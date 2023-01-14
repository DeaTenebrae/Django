from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.shortcuts import redirect
from hello.forms import LogMessageForm
from hello.models import LogMessage
from django.views.generic import ListView


class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


# def home(request):
#     return HttpResponse("Hello, Michelle!")

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "hello/log_message.html", {"form": form})

def hello(request):
    return HttpResponse("Hello, Django/Michelle!")

def it_is_me(request):
    return HttpResponse("Hello, it's me, hi I'm the HttpResponse!")

def hello_there(request, name):
    # now = datetime.now()
    # formatted_now = now.strftime("%A, %d %B, %Y at %X")
    # formatted_now2 = now.strftime("%X now, today a %A, exactly the %d. of %B, in the Year %Y")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)  # match_object.group(0) gibt die gesamte Gruppe an Zeichen zurück
    else:
        clean_name = "Friend"
    
    return render(request,'hello/hello_there.html',{'name': clean_name,'date': datetime.now()})

# def hello_there(request, name):    
#     return render(request,'hello/hello_there.html',{'name': name,'date': datetime.now()})

# def hello_there(request, name):
#     print("http://127.0.0.1:8000/hello/VSCode")
#     print(f"http://127.0.0.1:8000/hello/{name}")
#     now = datetime.now()
#     formatted_now = now.strftime("%A, %d %B, %Y at %X")
#     formatted_now2 = now.strftime("%X now, today a %A, exactly the %d. of %B, in the Year %Y")

#     # Filter the name argument to letters only using regular expressions. URL arguments
#     # can contain arbitrary text, so we restrict to safe characters only.
#     match_object = re.match("[a-zA-Z]+", name)

#     if match_object:
#         clean_name = match_object.group(0)  # match_object.group(0) gibt die gesamte Gruppe an Zeichen zurück
#     else:
#         clean_name = "Friend"
    

#     content = "Hello there, " + clean_name + "! It's " + formatted_now  + "<br> <br>in other words, " + clean_name + ", it's " + formatted_now2
#     return HttpResponse(content)

    