from django.db import models

class UploadFileModel(models.Model):
	title = models.CharField(max_length=256,null=True)
	file = models.FileField()
	def __str__(self):
		return str(self.title)