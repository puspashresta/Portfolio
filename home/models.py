from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=250)
    subject = models.TextField(blank=True)
    message = models.TextField()

    def __str__(self):
        return self.name

class Information(models.Model):
    address=models.CharField(max_length=300)
    local=models.CharField(max_length=300)
    phone=models.CharField(max_length=300)
    timing=models.CharField(max_length=300)
    email=models.CharField(max_length=300)

    def __str__(self):
        return self.address


class Reviews(models.Model):
    review=models.TextField()
    name=models.CharField(max_length=200)
    post=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Feedbacks(models.Model):
    commen=models.TextField()
    names=models.CharField(max_length=200)
    posts=models.CharField(max_length=200)

    def __str__(self):
        return self.names
