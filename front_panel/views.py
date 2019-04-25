from django.shortcuts import render,HttpResponse,redirect
from front_panel.forms import MySite_UserForm,Login_detailsForm
from front_panel.models import MySite_User,Login_details
from nutritionist.models import recipe_procedure_tb,recipes,category
from datetime import datetime
from miscellaneous import otp_generate as og, otp_send as os
import random
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.


def index(request):
        if (request.method == "POST"):
            useremail = request.POST['user_email']
            userpassword = request.POST['user_password']

            try:
                userdata = MySite_User.objects.get(user_email=useremail)
                dp = userdata.user_password
                uname = userdata.user_name
                mob=str(userdata.user_mobile)
                verified = userdata.is_verified
                authtoken=userdata.user_token
                auth_pass=check_password(userpassword,dp)
                if(auth_pass==True):
                    if verified== False and authtoken=="":
                        rn = random.randint(100000,10000000)
                        token= useremail[0:5] + str(rn)+mob[5:10]
                        verify = "http://127.0.0.1:8000/clicktoverifyyouraccount?email="+useremail+"&token="+token
                        os.email(useremail, "verification link", verify)
                        update =MySite_User(user_email=useremail, user_token= token)
                        update.save(update_fields=["user_token"])
                        return render(request,"home.html",{'login': True,'v1':True})


                    elif verified ==True:
                            userroleid = userdata.role_id_id
                            request.session['authenticated'] = True
                            request.session['emailid'] = useremail
                            request.session['roleid']= userroleid

                            email = request.session['emailid']
                            log_obj = Login_detailsForm(request.POST)
                            if log_obj.is_valid():
                                f = log_obj.save(commit=False)
                                f.user_name = email
                                f.login_time = str(datetime.now())
                                f.save()
                            log_id_data=Login_details.objects.filter(user_name=email).order_by('-login_id')[0:1]
                            lgid=0
                            for i in log_id_data:
                                lgid=i.login_id
                            request.session['login_id']=lgid
                            if(userroleid == 1):
                                return redirect("/admin_panel/admin_index")
                            elif (userroleid == 2):
                                return redirect("/nutritionist/nutri_index")
                            elif(userroleid == 3):
                                return redirect("/")
                            elif (userroleid == 4):
                                return redirect("/fitness_panel/index_fitness")

                else:
                    return render(request,"home.html",{'wrong_pass':True})
            except:
                return render(request,"page_not_found.html")

        return render(request, "home.html")

def verify(request):
    try:

        email = request.GET['email']
        token = request.GET['token']
        userdata=MySite_User.objects.get(user_email=email)
        user_verify=userdata.is_verified
        if(user_verify == True):
            return render(request,"home.html",{"verified":True})
        else:
            dbtoken=userdata.user_token
            if(dbtoken==token):
                verified=True
                update=MySite_User(user_email=email,is_verified=verified,user_token="")
                update.save(update_fields=["is_verified","user_token"])
                return redirect("/")
            else:
                return redirect("/error/")
    except:
        return render (request,"home.html",{"valid":True})

def logout(request):

    log_id=request.session['login_id']
    log_obj = Login_detailsForm(request.POST)
    if log_obj.is_valid():
        data=Login_details.objects.get(login_id=log_id)
        updatedata=Login_details(
            login_id=log_id,
            logout_time=str(datetime.now())

        )
        updatedata.save(update_fields=["logout_time"])
        request.session['authenticated'] = False
    return redirect("/")


def signup(request):
    signupobj = MySite_UserForm()

    if (request.method == "POST"):
        enter_password=request.POST['user_password']
        conf_password=request.POST['confirm_password']
        if(enter_password==conf_password):
            password=make_password(conf_password)
        else:
            return render(request,"signup.html",{'wp':True})
        f = signupobj.save(commit=False)
        f.user_name = request.POST['user_name']
        f.user_email = request.POST['user_email']
        f.user_mobile = request.POST['user_mobile']

        f.user_password= password
        f.role_id_id = request.POST['role_id']
        f.user_sign_up = datetime.now()
        rn = random.randint(100000,10000000)
        token = request.POST['user_email'][0:5]+str(rn)+str(request.POST['user_mobile'][5:10])
        f.user_token=token
        verify ="http://127.0.0.1:8000/clicktoverifyyouraccount?email="+request.POST['user_email']+"&token="+token
        os.email(f.user_email,"verification link",verify)
        f.save()

        return redirect("/",{'sign_up':True})

    return render(request,"signup.html")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST["user_email"]
        entered_otp = request.POST["enter_otp"]
        try:
            userdata = MySite_User.objects.get(user_email=email)
            if(email!="" and entered_otp==""):
                otp_gen, otptime = og.otpgenerate()
                updatedata = MySite_User(
                    user_email=email,
                    otp=otp_gen,
                    otp_time=otptime
                )
                updatedata.save(update_fields=["otp", "otp_time"])
                os.otpsend(otp_gen, email, "new Otp", "do not share")
                return render(request, "forgot_password.html", {"otp_gen": True,"os":True,'em':email})
            elif(email!="" and entered_otp!=""):
                db_otp=userdata.otp
                new_password = request.POST["new_password"]
                conf_password = request.POST["confirm_password"]
                if(db_otp==entered_otp):

                    if(new_password==conf_password):
                        updatetable=MySite_User(
                            user_email=email,
                            user_password=make_password(conf_password)
                        )
                        updatetable.save(update_fields=["user_password"])
                        os.email(email,"password changed","your password changed successfully")
                        return render(request,"home.html",{"pu":True})
                    else:
                      return render(request,"forgot_password.html",{"wrong":True,"otp_gen": True,'em':email})
                else:
                    return render(request, "forgot_password.html", {"wrong_otp": True,"otp_gen": True,'em':email})
        except:
            return render(request,"forgot_password.html",{"not_sent":True,"cp":True})
    return render(request,"forgot_password.html",{'cp':True})


def recipes_page(request):
    recipe_data = recipes.objects.all()
    cat_data=category.objects.all()

    return render(request, "recipes.html",{'rd':recipe_data,'cd':cat_data})



def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")



def exercise(request):
    return render(request, "exercise.html")

def single(request):

    return render(request,"single.html")


def pagenotfound(request):
    return render(request,"page_not_found.html")
