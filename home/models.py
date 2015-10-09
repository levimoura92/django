from django.db import models

# Create your models here.
class Newsletter(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=True, null=True)
	#msg = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	def __unicode__(self):
		return self.email
