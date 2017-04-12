from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

class Game(models.Model):
	title = models.CharField(max_length=140)
	genre = models.CharField(max_length=140)
	date = models.DateTimeField()
	tag = models.ManyToManyField(Tag, blank=True)
	def __str__(self):
		return self.title

class Review(models.Model):
	text = models.TextField()
	date = models.DateTimeField()
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	writer = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.text

class List(models.Model):
	name = models.CharField(max_length=100)
	games = models.ManyToManyField(Game)
	def __str__(self):
		return self.name

class Transaction(models.Model):
	buyer = models.ForeignKey(User, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	date = models.DateTimeField()
	def __str__(self):
		return str(self.date)
