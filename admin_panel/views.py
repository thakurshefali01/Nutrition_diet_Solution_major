from django.shortcuts import render,redirect
from admin_panel.forms import signup_AdminForm
from django.core.files.storage import FileSystemStorage
from miscellaneous import authorize as au
from front_panel.models import ContactTable

# Create your views here.

def admin_index(request):
    auth = au.authorizeuser(request.session["authenticated"], request.session["roleid"],1 )
    if (auth==True):
        return render(request, "index_admin.html")
    else:
        aut,message=auth
        if(message=="Wrong user Type"):
            return redirect("/wronguser/")
        elif(message=="Not login"):
            return redirect("/notlogin/")



def user_query(request):
    contact_data=ContactTable.objects.all()
    return render (request,"user_query.html",{'cd':contact_data})


