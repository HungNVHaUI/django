from django.urls import path
from .import views
from django.conf import settings

app_name = 'loadfile'

urlpatterns = [
	path('' , views.UploadFile.as_view(), name = 'UploadFile'),
	#path('post_upload/' , views.post_upload, name = 'post_upload'),
]
