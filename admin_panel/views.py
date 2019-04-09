from django.shortcuts import render,redirect
from admin_panel.forms import signup_AdminForm
from admin_panel.models import signup_Admin
from django.core.files.storage import FileSystemStorage
import authorize as au
# Create your views here.

def admin_index(request):
    auth = au.authorizeuser(request.session["authenticated"], request.session["emailid"], request.session["roleid"], )
    if (auth):
        return render(request, "index_admin.html")
    else:
        aut,message=auth
        if(message=="Wrong user Type"):
            return redirect("/wronguser/")
        elif(message=="Not login"):
            return redirect("/notlogin/")



def signup_admin(request):
    if (request.method == "POST"):
        form = signup_AdminForm(request.POST)
        user_image = None
        try:
            if request.FILES['admin_image']:
                myfile = request.FILES['admin_image']
                fs = FileSystemStorage()
                filename = fs.save( myfile.name,myfile)
                user_image = fs.url(filename)
                user_image=myfile.name
        except:
            pass
        if form.is_valid():
            f=form.save(commit=False)
            f.admin_email = request.POST['admin_email']
            f.admin_image=user_image
            f.admin_name= request.POST['admin_name']
            f.admin_password= request.POST['admin_password']
            f.admin_mobile= request.POST['admin_mobile']
            f.save()
            return render(request,"index_admin.html",{'inserted':True})
    return render(request, "signup_admin.html")

def login_admin(request):
    return render(request, "login_admin.html")

