from django.db import models

# Create your models here.

class Pptx( models.Model ):
	pptxname_text = models.CharField(max_length=200)
	pptx_file = models.BinaryField( blank=True, editable=False)
	pptx_size = models.CharField(max_length=100)
	pptx_thumbnail = models.ImageField( upload_to='images/%Y/%m/%d/')

	def __str__(self):
		return self.pptxname_text

