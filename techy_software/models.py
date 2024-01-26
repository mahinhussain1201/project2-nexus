from django.db import models

# Create your models here.

class Service(models.Model):
    icon = models.ImageField()
    heading = models.TextField(default="No heading available")
    content = models.TextField(default="No content available")

    def __str__(self):
        return self.heading

class Portfolio(models.Model):
    image = models.ImageField()
    type = models.TextField(default="Not available")
    heading = models.TextField(default="No heading available")

    def __str__(self):
        return self.heading

class Feedback(models.Model):
    content = models.TextField(default="No content available")
    image = models.ImageField()
    name = models.TextField(default="No name available")
    country = models.TextField(default="No country available")

    def __str__(self):
        return self.name

class Blog(models.Model):
    image = models.ImageField()
    author = models.TextField(default="No author available")
    date = models.DateField()
    heading = models.TextField(default="No heading available")
    content = models.TextField(default="No content available")

    def __str__(self):
        return self.heading
    
class Team(models.Model):
    image = models.ImageField()
    name = models.TextField()
    
    def __str__(self):
        return self.name
  
class SaveFeedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()
    
    def __str__(self):
        return self.name
    
class Subscribe(models.Model):
    email=models.EmailField()
    
    def __str__(self):
        return self.email
    