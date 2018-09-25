from django.db import models

class DataInput(models.Model):
	number = models.CharField(max_length=5)
	time_stamp = models.CharField(max_length=255)

	class Meta:
		app_label = 'datainput'