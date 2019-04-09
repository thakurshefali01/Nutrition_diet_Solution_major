from django.conf.urls import url
from admin_panel import views

app_name='admin_panel'

urlpatterns=[
        url(r'^admin_index/$',views.admin_index,name="admin_index"),
        url(r'^login_admin/$',views.login_admin,name="login_admin"),
        url(r'^adminsignup/$',views.signup_admin,name="signup_admin"),

]