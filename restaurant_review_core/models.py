from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    total_score = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"Name: {self.name}, Address: {self.address}"


class Review(models.Model):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.PositiveSmallIntegerField(
        default=0, validators=[MaxValueValidator(10)]
    )

    def __str__(self):
        return f"Score: {self.score}, Text: {self.text}"
