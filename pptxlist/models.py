from django.db import models

# Create your models here.

class Pptx( models.Model ):
	pptxname_text = models.CharField(max_length=200)

