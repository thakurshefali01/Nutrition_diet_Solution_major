from django.conf.urls import url
from Fitness_panel import views

app_name='Fitness_panel'

urlpatterns=[
        url(r'^index_fitness/$',views.index_fitness,name="index_fitness")

]