from django.shortcuts import render,redirect
from admin_panel.forms import signup_AdminForm
from django.core.files.storage import FileSystemStorage
from miscellaneous import authorize as au
from front_panel.models import ContactTable,MySite_User,Login_details

# Create your views here.

def admin_index(request):
    auth = au.authorizeuser(request.session["authenticated"], request.session["roleid"],1 )
    if (auth==True):
        emailid= request.session['emailid']
        data = MySite_User.objects.get(user_email=emailid)

        user =MySite_User.objects.filter(role_id =3).count()
        nutritionist =MySite_User.objects.filter(role_id =2).count()
        fitness = MySite_User.objects.filter(role_id=4).count()
        visitors = Login_details.objects.all().count()
        return render(request, "index_admin.html",{'gd':data,'user':user,'nutri':nutritionist,'fitness':fitness,'visitors':visitors})
    else:
        aut,message=auth
        if(message=="Wrong user Type"):
            return redirect("/wronguser/")
        elif(message=="Not login"):
            return redirect("/notlogin/")



def user_query(request):
    contact_data=ContactTable.objects.all()
    return render (request,"user_query.html",{'cd':contact_data})


