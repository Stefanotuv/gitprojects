from django.db import models
import os

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','st1.settings')

import django
# Import settings
django.setup()
# Create your models here.

# import the classes from the models
from exercise.models import AppUser, UserActivities

# classes to generate fake contents
import random
from faker import Faker
fakegen = Faker()

def populate(N):
    '''
    Create N Entries of Dates Accessed
    '''
    for entry in range(N):
        # Create Fake Data for entry
        # fake_name = fakegen.name().split()
        # fake_first_name = fake_name[0]
        # fake_last_name = fake_name[-1]
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()

        fake_email = fakegen.email()
        print(fake_email)
        fake_date = fakegen.date()

        # Create new User Entry
        user = AppUser.objects.get_or_create(name=fake_first_name,surname=fake_last_name,email=fake_email)[0]
        user.save()
        UserActivities.objects.get_or_create(appUser=user,date=fake_date)







if __name__ == '__main__':
    # print("something")
    # testUser = AppUser()
    # # testActivity = UserActivities()
    #
    # testUser.name = "stefano"
    # testUser.surname = "tuveri"
    # # testActivity.user = testUser
    # # testActivity.date = fakegen.date()
    #
    # print(testUser)
    # print('something else')
    print("Populating the databases...Please Wait")
    populate(100)
    # populate(100)
    print('Populating Complete')
