from django.db import models

# Create your models here.
class postBlog(models.Model):
	title = models.CharField(max_length=256, null=True)
	body = models.TextField()
	image = models.ImageField(upload_to='image/', blank=True, null=True)
	create_at = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return str(self.title)
