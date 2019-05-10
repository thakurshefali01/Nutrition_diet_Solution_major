from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from miscellaneous import authorize as au
from nutritionist.models import ExerciseCategory, AddExercise
from Fitness_panel.froms import Add_exerciseForm

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


def Add_exercise_fun(request):
    userdata=ExerciseCategory.objects.all()
    if (request.method == "POST"):
        exerciseimage = None
        if request.FILES:
            myfile = request.FILES['Exercise_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            fs.url(filename)
            exerciseimage = myfile.name
        form = Add_exerciseForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.exercise_image = exerciseimage
            f.exercise_name = request.POST['Exercise_name']
            f.exercise_discription = request.POST['Exercise_discription']
            f.exercise_price = request.POST['Exercise_price']
            f.exercise_id_id = request.POST['Exercise_category']
            f.user_email_id = request.session['emailid']
            f.save()
        return render(request, "add_exercise.html", {'inserted': True,'ud':userdata})
    return render(request,"add_exercise.html",{'ud':userdata})

def view_exercise(request):
    email_id= request.session['emailid']
    view_data=AddExercise.objects.filter(user_email=email_id)
    return render(request,"view_exercise.html",{'vd':view_data})

def delete(request):
    exerciseId=request.GET['id']
    try:
        deleteUser=AddExercise.objects.get(add_exercise_id=exerciseId)
        deleteUser.delete()
        return redirect("/fitness_panel/view_exercise/")
    except:
        pass

def edit_exercise(request):
    editdata = ExerciseCategory.objects.all()
    edit_id = request.GET['id']
    get_data = AddExercise.objects.get(add_exercise_id=edit_id)
    if request.method=="POST":
        exerciseimage = None
        if request.FILES:
            myfile = request.FILES['exercise_image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            fs.url(filename)
            exerciseimage = myfile.name
        exercise_id= request.POST['exercise_category']
        name = request.POST['exercise_name']
        description = request.POST['exercise_description']
        image=exerciseimage
        update = AddExercise(add_exercise_id=edit_id, exercise_id_id=exercise_id,exercise_name=name, exercise_discription=description,exercise_image=image)
        update.save(update_fields=["exercise_id_id","exercise_name","exercise_discription","exercise_image"])
        return redirect("/fitness_panel/view_exercise/")
    return render(request,"edit_exercise.html", {'gt':get_data,'exd':editdata})