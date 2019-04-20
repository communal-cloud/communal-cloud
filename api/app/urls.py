"""app URL Configuration

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
from django.conf.urls import url, include
from rest_framework import routers

from api.cc.Controllers.CategoryController import CategoryController
from api.cc.Controllers.CommunityController import CommunityController
from api.cc.Controllers.DataController import DataController
from api.cc.Controllers.ExecutionController import ExecutionController
from api.cc.Controllers.RoleController import RoleController
from api.cc.Controllers.ServiceController import ServiceController
from api.cc.Controllers.TaskController import TaskController
from api.cc.Controllers.UserController import UserController
from api.cc.Controllers.WorkflowController import WorkflowController

router = routers.DefaultRouter()

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^admin/', admin.site.urls),
	url(r'^service/$', ServiceController.as_view()),
	url(r'^user/$', UserController.as_view()),
	url(r'^category/$', CategoryController.as_view()),
	url(r'^community/$', CommunityController.as_view()),
	url(r'^data/$', DataController.as_view()),
	url(r'^execution/$', ExecutionController.as_view()),
	url(r'^role/$', RoleController.as_view()),
	url(r'^task/$', TaskController.as_view()),
	url(r'^workflow/$', WorkflowController.as_view()),
]
