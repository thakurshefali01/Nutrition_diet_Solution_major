from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
import authorize as au
from nutritionist.forms import recipesForm ,recipe_procedure_tbForm
from nutritionist.models import category,recipes,recipe_procedure_tb
from front_panel.models import MySite_User
# Create your views here.
def index_nutri(request):
    try:
        auth = au.authorizeuser(request.session["authenticated"], request.session["roleid"],1)
    except:
        return redirect("/notlogin/")

    if (auth):
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


def view_recipe(request):
    view_data=recipes.objects.all()
    return render(request,"view_recipe.html",{'vd':view_data})


def delete(request):
    recipeId=request.GET['id']
    try:
        deleteUser=recipes.objects.get(recipe_id=recipeId)
        deleteUser.delete()
        return redirect("/view_recipe/")
    except:
        pass

def add_procedure(request):
    if (request.method == "POST"):
        robj=recipes.objects.all()
        pro_obj = recipe_procedure_tbForm()
        f = pro_obj.save(commit=False)
        f.recipe_name=request.POST['recipe_name']
        f.procedure_discription = request.POST['recipe_description']
        f.prep_time = request.POST['prepration_time']
        f.cook_time=request.POST['cook_time']
        f.procedure_ingredients = request.POST['recipe_ingredients']
        f.procedure_instructions = request.POST['recipe_instructions']
        f.procedure_notes = request.POST['recipe_note']
        f.user_email_id=request.session['emailid']
        f.recipe_id_id=request.GET['id']
        f.save()

        update = recipes(recipe_id=f.recipe_id_id,recipe_isProcedure=1)
        update.save(update_fields=["recipe_isProcedure"])
        return redirect("/view_recipe/",{'inserted': True})
    return render(request, "add_procedure.html" )

def view_procedure(request):

    viewPro_Obj=request.GET['id']

    return render(request, "view_procedure.html",{'vp':viewPro_Obj})