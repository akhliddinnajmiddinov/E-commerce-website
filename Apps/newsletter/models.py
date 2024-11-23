from django.db import models


class Subscriber(models.Model):
	email = models.CharField(max_length = 100, unique=True)
	date_created = models.DateTimeField(auto_now_add = True)

	
	def __str__(self):
		return self.email