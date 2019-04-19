from django.conf.urls import url
from nutritionist import views

app_name='nutritionist'

urlpatterns=[
    url(r'^nutri_index/$', views.index_nutri, name="nutri_index"),
    url(r'^add_recipe/$',views.add_recipe,name="add_recipe"),
    url(r'^view_recipe/$',views.view_recipe,name="view_recipe"),
    url(r'^add_procedure/$',views.add_procedure,name="add_procedure"),
    url(r'^view_procedure/$',views.view_procedure,name="view_procedure"),
    url(r'^delete/$',views.delete,name="delete"),
    url(r'^edit_recipe/$',views.edit_recipe,name="edit_recipe"),
    url(r'^edit_procedure/$',views.edit_procedure,name="edit_procedure"),
    url(r'^change_password/$',views.change_password,name="change_password")
]