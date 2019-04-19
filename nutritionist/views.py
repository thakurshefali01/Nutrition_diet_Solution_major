from django.shortcuts import render,redirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from miscellaneous import authorize as au,otp_generate as og,otp_send as os

from nutritionist.forms import recipesForm ,recipe_procedure_tbForm
from nutritionist.models import category,recipes,recipe_procedure_tb
from front_panel.models import MySite_User
import smtplib
from datetime import datetime

def index_nutri(request):
    try:
        auth = au.authorizeuser(request.session["authenticated"], request.session["roleid"],2)
    except:
        return redirect("/notlogin/")

    if (auth==True):
        return render(request, "index_nutri.html")
    else:
        aut, message = auth
        if (message == "Wrong user Type"):
            return redirect("/wronguser/")
        elif (message == "Not login"):
            return redirect("/notlogin/")


def add_recipe(request):
    userdata=category.objects.all()
    addobj = recipesForm()
    if (request.method == "POST"):
        recipeimage = None
        if request.FILES:
            myfile = request.FILES['recipe_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            fs.url(filename)
            recipeimage = myfile.name

        form = recipesForm(request.POST)
        if form.is_valid():

            f = form.save(commit=False)
            f.recipe_image = recipeimage
            f.recipe_name = request.POST['recipe_name']
            f.recipe_description = request.POST['recipe_description']
            f.recipe_isactive = 1
            f.category_id_id = request.POST['recipe_category']
            f.user_email_id = request.session['emailid']
            f.save()
        return render(request, "add_recipies.html", {'inserted': True,'ud':userdata})



    return render(request,"add_recipies.html",{'ud':userdata})


def add_procedure(request):
    if (request.method == "POST"):
        robj=recipes.objects.all()
        pro_obj = recipe_procedure_tbForm()
        f = pro_obj.save(commit=False)
        f.recipe_name=request.POST['recipe_name']
        f.procedure_discription = request.POST['recipe_description']
        f.prep_time = request.POST['prepration_time']
        f.cook_time=request.POST['cook_time']
        f.total_time = request.POST['total_time']
        f.procedure_ingredients = request.POST['recipe_ingredients']
        f.procedure_instructions = request.POST['recipe_instructions']
        f.procedure_notes = request.POST['recipe_note']
        f.user_email_id=request.session['emailid']
        f.recipe_id_id=request.GET['id']
        f.save()

        update = recipes(recipe_id=f.recipe_id_id,recipe_isProcedure=1)
        update.save(update_fields=["recipe_isProcedure"])
        return redirect("/nutritionist/view_recipe/",{'inserted': True})
    return render(request, "add_procedure.html" )


def view_recipe(request):
    email_id= request.session['emailid']
    view_data=recipes.objects.filter(user_email=email_id)
    return render(request,"view_recipe.html",{'vd':view_data})

def view_procedure(request):

    r_id=request.GET['id']
    pro_data=recipe_procedure_tb.objects.filter(recipe_id=r_id)
    return render(request, "view_procedure.html",{'pd':pro_data})


def delete(request):
    recipeId=request.GET['id']
    try:
        deleteUser=recipes.objects.get(recipe_id=recipeId)
        deleteUser.delete()
        return redirect("/nutritionist/view_recipe/")
    except:
        pass

def edit_recipe(request):
    editdata = category.objects.all()
    edit_id = request.GET['id']
    get_data = recipes.objects.get(recipe_id=edit_id)
    if request.method=="POST":
        recipeimage = None
        if request.FILES:
            myfile = request.FILES['recipe_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            fs.url(filename)
            recipeimage = myfile.name
        category_id= request.POST['recipe_category']
        name = request.POST['recipe_name']
        description = request.POST['recipe_description']
        image=recipeimage
        update = recipes(recipe_id=edit_id, category_id_id=category_id,recipe_name=name, recipe_description=description,recipe_image=image)
        update.save(update_fields=["category_id_id","recipe_name","recipe_description","recipe_image"])
        return redirect("/nutritionist/view_recipe/")
    return render(request,"edit.html", {'vt':get_data,'ed':editdata})



def edit_procedure(request):
    edit_id = request.GET['id']
    get_data = recipe_procedure_tb.objects.get(procedure_id=edit_id)
    if request.method == "POST":
        name=request.POST['recipe_name']
        description=request.POST['recipe_discription']
        prep_time=request.POST['prepration_time']
        cook_time=request.POST['cook_time']
        total_time=request.POST['total_time']
        ingredients=request.POST['recipe_ingredients']
        instructions=request.POST['recipe_instructions']
        notes=request.POST['recipe_note']

        update = recipe_procedure_tb(
            procedure_id=edit_id,
            recipe_name=name,
            procedure_discription=description,
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            procedure_ingredients=ingredients,
            procedure_instructions=instructions,
            procedure_notes=notes
        )
        update.save(update_fields=["recipe_name","procedure_discription","prep_time","cook_time","total_time","procedure_ingredients","procedure_instructions","procedure_notes"])
        return redirect("/nutritionist/view_recipe/")
    return render(request,"edit_procedure.html",{'gd':get_data})

def change_password(request):

    emailid = request.session["emailid"]

    if(request.method=="POST"):


        opassword=request.POST['old_password']
        npassword=request.POST['new_password']
        confpass=request.POST['confirm_password']
        new_otp=request.POST['otp']
        userdata = MySite_User.objects.get(user_email=emailid)
        otp_db = userdata.otp
        if (otp_db == new_otp):


            if (npassword==confpass):

                dbpass=userdata.user_password

                if(dbpass==opassword):

                        updatedata=MySite_User(
                        user_email=emailid,
                        user_password=npassword
                        )
                        updatedata.save(update_fields=["user_password"])

                        try:
                            os.email(emailid,"confirmation mail","password changed successfully")
                            return redirect("/nutritionist/nutri_index/")
                        except:
                            return HttpResponse("<h1>Email sending failed</h1>")

                else:
                    return render(request,"change_password.html",{'op':"wrong old password"})

            else:
                return render(request,"change_password.html",{'password':"password did not match"})
        else:
            return render(request, "page_not_found.html", {'otp': "wrong otp"})
    else:
        otp_gen,otptime = og.otpgenerate()
        updatedata = MySite_User(
            user_email=emailid,
            otp=otp_gen,
            otp_time=otptime
        )
        updatedata.save(update_fields=["otp","otp_time"])
        os.otpsend(otp_gen, emailid, "new Otp", "do not share")

    return render(request,"change_password.html")


