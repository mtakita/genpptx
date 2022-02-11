from django.urls import path, include

from . import views

app_name = 'pptxlist'

urlpatterns = [
	path('', views.index, name='index'),
	path('uploadform', views.uploadform, name='uploadform'),
	path('upload', views.upload, name='upload'),
	path('<int:pptx_id>/genpptx', views.genpptx, name='genpptx')
]

