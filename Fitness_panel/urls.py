from django.conf.urls import url
from Fitness_panel import views

app_name='Fitness_panel'

urlpatterns=[
        url(r'^index_fitness/$',views.index_fitness,name="index_fitness"),
        url(r'^add_exercise/$',views.Add_exercise_fun,name="add_exercise"),
        url(r'^view_exercise/$',views.view_exercise,name="view_exercise"),
        url(r'^delete/$',views.delete,name="delete"),
        url(r'^edit_exercise/$',views.edit_exercise,name="edit_exercise")


]