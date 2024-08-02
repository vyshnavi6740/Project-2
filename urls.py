"""cyber URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from cyber import views as admins
from user import views as usr

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admins.index, name='index'),
    path('Home/', admins.Home, name='Home'),
    path('adminlogin/', admins.adminlogin, name='adminlogin'),
    path('adminloginaction/', admins.adminloginaction, name='adminloginaction'),
    path('showusers/', admins.showusers, name='showusers'),

    path('logout/', admins.logout, name='logout'),
    path('populate_data/', admins.populate_data, name='populate_data'),
    path('accuracy/', admins.accuracy, name='accuracy'),

    path('Userlogin/', usr.Userlogin, name='Userlogin'),
    path('userregister/', usr.userregister, name='userregister'),
    path('userregisterAction/', usr.userregisterAction, name='userregisterAction'),
    path('userloginaction/', usr.userloginaction, name='userloginaction'),
    path('predict/', usr.predict, name='predict'),
    path('usrlogout/', usr.usrlogout, name='usrlogout'),
    path('svc_prediction/', usr.svc_prediction, name='svc_prediction'),
    path('predict1/', usr.predict1, name='predict1'),
    path('rfc_prediction/', usr.rfc_prediction, name='rfc_prediction'),
    path('predict2/', usr.predict2, name='predict2'),
    path('gbc_prediction/', usr.gbc_prediction, name='gbc_prediction'),
    path('predict3/', usr.predict3, name='predict3'),
    path('dnn_bert_prediction/', usr.dnn_bert_prediction, name='dnn_bert_prediction')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)