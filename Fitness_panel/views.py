from django.shortcuts import render,redirect
from miscellaneous import authorize as au
# Create your views here.
def index_fitness(request):
    try:
        auth = au.authorizeuser(request.session["authenticated"], request.session["roleid"],4)
    except:
        return redirect("/notlogin/")

    if (auth==True):
        return render(request, "index_fitness.html")
    else:
        aut, message = auth
        if (message == "Wrong user Type"):
            return redirect("/wronguser/")
        elif (message == "Not login"):
            return redirect("/notlogin/")

    return render(request, "index_fitness.html")