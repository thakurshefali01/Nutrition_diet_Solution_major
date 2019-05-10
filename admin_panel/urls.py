from django.conf.urls import url
from admin_panel import views

app_name='admin_panel'

urlpatterns=[
        url(r'^admin_index/$',views.admin_index,name="admin_index"),
        url(r'^user_query/$',views.user_query,name="user_query")

]