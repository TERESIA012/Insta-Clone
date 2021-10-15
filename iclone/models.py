from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
	bio = models.CharField(max_length = 300,blank = True,default = 'Awesome Bio Will Appear Here')
	profile_pic = models.ImageField(upload_to = 'profile/', blank = True,default = '../static/images/default.png')
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	

	def __str__(self):
		return self.user
