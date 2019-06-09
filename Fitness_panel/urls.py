from django.conf.urls import url
from Fitness_panel import views

app_name='Fitness_panel'

urlpatterns=[
        url(r'^index_fitness/$',views.index_fitness,name="index_fitness"),
        url(r'^add_exercise/$',views.Add_exercise_fun,name="add_exercise"),
        url(r'^view_exercise/$',views.view_exercise,name="view_exercise"),
        url(r'^delete/$',views.delete,name="delete"),
        url(r'^edit_exercise/$',views.edit_exercise,name="edit_exercise"),
        url(r'^add_exercise_procedure/$',views.add_exercise_procedure,name="add_exercise_procedure"),
        url(r'^edit_exercise_procedure/$',views.edit_exercise_procedure,name="edit_exercise_procedure"),
        url(r'^view_exercise_procedure/$',views.view_exercise_procedure,name="view_exercise_procedure"),



]