from django.shortcuts import render,HttpResponse,redirect
from front_panel.forms import MySite_UserForm
from front_panel.models import MySite_User

# Create your views here.
def index(request):
        if (request.method=="POST"):
            useremail=request.POST['user_email']
            userpassword=request.POST['user_password']

            try:
                userdata=MySite_User.objects.get(user_email=useremail)

                dp=userdata.user_password

                if(dp==userpassword):
                    userroleid = userdata.role_id_id
                    request.session['authenticated'] = True
                    request.session['emailid'] = useremail
                    request.session['roleid']= userroleid
                    if(userroleid==1):
                        return redirect("/admin_index/")
                    elif (userroleid ==2):
                        return redirect("/nutri_index/")
                    elif(userroleid==3):
                        return redirect("/")


            except:
                return render(request,"page_not_found.html")

        return render(request, "home.html")




def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def recipes(request):
    return render(request, "recipes.html")

def exercise(request):
    return render(request, "exercise.html")

def single(request):
    return render(request,"single.html")


def pagenotfound(request):
    return render(request,"page_not_found.html")


def signup(request):
    signupobj=MySite_UserForm()

    if (request.method=="POST"):

        f=signupobj.save(commit=False)
        f.user_name = request.POST['user_name']
        f.user_email = request.POST['user_email']
        f.user_mobile = request.POST['user_mobile']
        f.user_password= request.POST['user_password']
        f.role_id_id=request.POST['role_id']
        f.save()
        return render(request,"home.html",{'inserted':True})

    return render(request,"signup.html")


def logout(request):
    request.session['authenticated']=False
    return redirect("/")


def change_password(request):
    if(request.method=="POST"):
        emailid=request.session["emailid"]

        opassword=request.POST['old_password']
        npassword=request.POST['new_password']
        confpass=request.POST['confirm_password']
        if (npassword==confpass):
            userdata=MySite_User.objects.get(user_email=emailid)
            dbpass=userdata.user_password
            if(dbpass==opassword):

                upadtedata=MySite_User(
                    user_email=emailid,
                    user_password=npassword
                )
                upadtedata.save(update_fields=["user_password"])

                return redirect("/")

            else:
                return render(request,"change_password.html",{'op':"wrong"})

        else:
            return render(request,"change_password.html",{'password':"password did not match"})


    return render(request,"change_password.html")