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
from rest_framework.authtoken.views import ObtainAuthToken

from cc.Controllers.CategoryController import CategoryController
from cc.Controllers.CommunityController import CommunityController, CommunityViewSetController
from cc.Controllers.FieldClassController import FieldClassController
from cc.Controllers.ExecutionController import ExecutionController
from cc.Controllers.RoleController import RoleController
from cc.Controllers.ServiceController import ServiceController
from cc.Controllers.TaskController import TaskController
from cc.Controllers.UserController import UserAPIViewController, UserViewSetController, UserTaskController
from cc.Controllers.WorkflowController import WorkflowController, CommunityWorkflowController, \
	CommunityDataTypeController
from cc.views import TasksController, RolesController, AllCommunitiesController, \
	AllActiveCommunitiesController, MembersOfCommunityController
from cc.Controllers.MemberController import CommunityMemberController, RoleMemberController

router = routers.DefaultRouter()
router.register(r'', UserViewSetController, basename='user')
router.register(r'', CommunityViewSetController, basename='community')

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^admin/', admin.site.urls),
	url(r'^user/login', ObtainAuthToken.as_view()),
	url(r'^user/$', UserAPIViewController.as_view()),
	url(r'^user/communities/(?P<id>.+)/tasks/$', UserTaskController.as_view()),
	url(r'^service/$', ServiceController.as_view()),
	url(r'^category/$', CategoryController.as_view()),
	url(r'^community/(?P<id>.+)/roles/$', RolesController.as_view()),
	url(r'^community/all/$', AllCommunitiesController.as_view()),
	url(r'^community/allActive/$', AllActiveCommunitiesController.as_view()),
	url(r'^community/$', CommunityController.as_view()),
	url(r'^community/(?P<id>.+)/workflow/$', CommunityWorkflowController.as_view()),
	url(r'^community/(?P<id>.+)/datatype/$', CommunityDataTypeController.as_view()),
	url(r'^community/(?P<id>.+)/members', MembersOfCommunityController.as_view()),
	url(r'^community/(?P<id>.+)/$', CommunityController.as_view()),
	url(r'^data/(?P<id>.+)/$', FieldClassController.as_view()),
	url(r'^execution/(?P<id>.+)/$', ExecutionController.as_view()),
	url(r'^execution/$', ExecutionController.as_view()),
	url(r'^role/(?P<id>.+)/$', RoleController.as_view()),
	url(r'^task/(?P<id>.+)/$', TaskController.as_view()),
	url(r'^workflow/(?P<id>.+)/tasks/$', TasksController.as_view()),
	url(r'^workflow/(?P<id>.+)/$', WorkflowController.as_view()),
	url(r'^member/(?P<id>.+)/communities/$', CommunityMemberController.as_view()),
	url(r'^member/(?P<id>.+)/roles/$', RoleMemberController.as_view())
]
