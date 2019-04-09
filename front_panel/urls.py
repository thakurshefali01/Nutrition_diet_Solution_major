from django.conf.urls import url
from front_panel import views

app_name='front_panel'

urlpatterns=[
        url(r'^$',views.index,name="index"),
        url(r'^about/$',views.about,name="about"),
        url(r'^recipes/$',views.recipes,name="recipes"),
        url(r'^contact/$',views.contact,name="contact"),
        url(r'^exercise/$',views.exercise,name="excercise"),
        url(r'^single/$',views.single,name="single"),
        url(r'^signup/$',views.signup,name="signup"),
        url(r'^logout/$',views.logout,name="logout"),
        url(r'^error/$',views.pagenotfound,name="error"),
        url(r'^change_password/$',views.change_password,name="change_password")


]