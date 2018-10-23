from django.db import models
import os

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','st1.settings')

import django
# Import settings
django.setup()
# Create your models here.
from exercise.models import AppUser
#
# from faker import Faker
# fakegen = Faker()
# class Topic(models.Model):
#     top_name = models.CharField(max_length=264,unique=True)
#
#     def __str__(self):
#         return self.top_name
#
# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic)
#     name = models.CharField(max_length=264,unique=True)
#     url = models.URLField(unique=True)
#
#     def __str__(self):
#         return self.name
#
# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage)
#     date = models.DateField()
#
#     def __str__(self):
#         return str(self.date)

# class AppUser(models.Model):
#
#     name = models.CharField(max_length=264,unique=True)
#     surnaname = models.CharField(max_length=264,unique=True)
#     email = models.EmailField(max_length=70,blank=True)
#
#     def __str__(self):
#         return sstr(self.name +" "+self.surname)
#
# Test = AppUser()
#
# print(Test)

if __name__ == '__main__':
    print("something")
    testUser = AppUser()
    # testActivity = UserActivities()

    testUser.name = "stefano"
    testUser.surname = "tuveri"
    # testActivity.user = testUser
    # testActivity.date = fakegen.date()

    print(testUser)
    print('something else')
