from django.urls import path, include

from . import views

app_name = 'emplist'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:employee_id>/detail', views.detail, name='detail'),
	path('<int:employee_id>/genpptx', views.genpptx, name='genpptx'),
	path('registform', views.registform, name='registform'),
	path('regist', views.regist, name='regist'),
]
