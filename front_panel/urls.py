from django.conf.urls import url
from front_panel import views

app_name='front_panel'

urlpatterns=[
        url(r'^$',views.index,name="index"),
        url(r'^about/$',views.about,name="about"),
        url(r'^recipes/$',views.recipes_page,name="recipes"),
        url(r'^contact/$',views.contact,name="contact"),
        url(r'^exercise/$',views.exercise_page,name="excercise"),
        url(r'^single/$',views.single,name="single"),
        url(r'^signup/$',views.signup,name="signup"),
        url(r'^logout/$',views.logout,name="logout"),
        url(r'^error/$',views.pagenotfound,name="error"),
        url(r'^forgot_password/$',views.forgot_password,name="forgot_password"),
        url(r'^clicktoverifyyouraccount?/$',views.verify,name="verify_link"),
        url(r'^user_profile/$', views.user_profile, name="user_profile"),
        url(r'^update_profile/$', views.update_profile, name="update_profile"),
        url(r'^change_password/$', views.change_password, name="change_password"),
        url(r'^show_cart/$', views.show_cart, name="show_cart"),
        url(r'^cart/$', views.cart, name="cart"),
        url(r'^cart1/$', views.cart1, name="cart1"),
        url(r'^charts/$', views.charts, name="charts"),
        url(r'^remove_item/$', views.remove_item, name="remove_item"),


]