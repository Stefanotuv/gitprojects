from django.db import models
import random

class AppUser(models.Model):
    name = models.CharField(max_length=264)
    surname = models.CharField(max_length=264)
    email = models.EmailField(max_length=70,unique=True,blank=True)
    def __str__(self):
        return str(self.name +" "+self.surname)

class SiteType(models.Model):
    type = models.CharField(max_length=264,unique=True)
    # def __init__(self):
    #      topics = ['Search','Social','Marketplace','News','Games']
    #      self.type = random.choice(topics)
    def __str__(self):
        return str(self.type)

class Website(models.Model):
    # visited website
    sitetype = models.ForeignKey(SiteType,on_delete=models.CASCADE)
    url = models.URLField()

class UserActivities(models.Model):
    appUser = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    webstVisited = models.ForeignKey(Website,default="",on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
