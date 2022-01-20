from django.shortcuts import render

from .models import Pptx

# Create your views here.

def index(request):
	pptx_list = Pptx.objects.all()
	return render(request, 'pptxlist/list.html', { 'pptx_list': pptx_list })

def uploadform(request):
	return render(request, 'pptxlist/uploadform.html' )

