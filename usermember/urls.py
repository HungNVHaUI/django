from django.urls import path
from .import views
app_name = 'usermember'

urlpatterns = [
    path('' , views.loginUser.as_view(), name = 'login'),
    path('register/' , views.registerUser.as_view(), name = 'register'),
	path('logout/' ,views.logoutUser, name = 'logout'),
	path('private/' ,views.privatePage.as_view(), name = 'private'),
]