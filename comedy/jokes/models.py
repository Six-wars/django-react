from django.db import models

class DadJokes(models.Model):
	text = models.TextField(unique=True)

	def __str__(self):
		return self.text

class Tweet(models.Model):
	text = models.TextField(unique=True)

	def __str__(self):
		return self.text

class Joke(models.Model):
	text = models.TextField(unique=True)

	def __str__(self):
		return self.text