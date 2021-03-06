"""Nutrition_diet_Solution_major URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import  static
from front_panel import views
from django.views.generic import TemplateView


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^',include('front_panel.urls')),
    url(r'^admin_panel/',include('admin_panel.urls')),
    url(r'^nutritionist/', include('nutritionist.urls')),
    url(r'^fitness_panel/', include('Fitness_panel.urls')),
    url(r'^paypal/',include('paypal.standard.ipn.urls')),
    url(r'^payment_process/$',views.payment_process,name='payment_process'),
    url(r'^payment_done/$',views.saledata,name='payment_done'),
    url(r'^payment_canceled/$',TemplateView.as_view(template_name="payment_canceled.html"),name='payment_canceled')

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
