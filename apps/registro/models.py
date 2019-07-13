from django.db import models
class Universitario(models.Model):
	paterno = models.CharField(max_length=10)
	materno = models.CharField(max_length=10)
	nombres = models.CharField(max_length=20)