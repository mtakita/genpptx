from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm

from .models import Pptx

import os

from thumbnail import generate_thumbnail

# Create your views here.

from .funcs import handle_uploaded_file

from tempfile import NamedTemporaryFile

from PIL import Image


def index(request):
	pptx_list = Pptx.objects.all()
	return render(request, 'pptxlist/list.html', { 'pptx_list': pptx_list })

def uploadform(request):
	return render(request, 'pptxlist/uploadform.html' )

def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():

			myByteArray = bytearray()

			myByteArray = handle_uploaded_file(request.FILES['file'])

		#	file = request.FILES['file']
		#	file = form.cleaned_data.get('file')
		#	file.seek(0, os.SEEK_END)


			#####################
			# Generate thumbnail 
			#####################
			with open("test.pptx", "wb" ) as binary_file:
				binary_file.write( myByteArray )
				binary_file.close()

			options = { 
				'trim': False,
				'height': 300,
				'width': 300,
				'quality': 85,
				'type': 'thumbnail'
			}

			generate_thumbnail( 'test.pptx', 'thumbnail.png', options )

			img_file = open( 'thumbnail.png', 'rb' )

			pptx = Pptx( pptxname_text = request.POST['title'], pptx_file = myByteArray, pptx_size = len(myByteArray) )

			pptx.pptx_thumbnail.save( 'thumbnail.png', content=img_file )
			pptx.save()

			img_file.close()


			


			pptx_list = Pptx.objects.all()
			return render(request, 'pptxlist/list.html', {'pptx_list': pptx_list})
	else:
		form = UploadFileForm()

	pptx_list = Pptx.objects.all()
	return render(request, 'pptxlist/list.html', {'pptx_list': pptx_list})

def genpptx(request, pptx_id ):

	pptx = Pptx.objects.get( pk=pptx_id )

	with open("test.pptx", "wb" ) as binary_file:
		binary_file.write( pptx.pptx_file )
		binary_file.close()

	file = open("test.pptx", "rb" )
	response = HttpResponse( file.read(), content_type = "application/pptx" )
	response['Content-Disposition'] = 'attachment; filename=%s' % pptx.pptxname_text + '.pptx'
	return response


	
def show_image( request, img ):
	context = {
		'image' : img
	}
	return render( request, 'image.html', context )

