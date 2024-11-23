from django.db import models

class Coupon(models.Model):
	code = models.CharField(max_length=50, unique=True)
	value = models.IntegerField()
	active = models.BooleanField(default=True)
	num_available = models.IntegerField(default=1)
	num_used = models.IntegerField(default=0)


	def can_use(self):
		return self.active and self.num_used < self.num_available

	def use(self):
		self.num_used += 1
		if self.num_used == self.num_available:
			self.active = False

		self.save()


	def __str__(self):
		return self.code