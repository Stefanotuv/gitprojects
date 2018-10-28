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
from exercise.models import AppUser, UserActivities, Website, SiteType

# classes to generate fake contents
import random
from faker import Faker
fakegen = Faker()

def populateSiteTypes():
    print('inside populateSiteTypes')
    topics = ('Search','Social','Marketplace','News','Games')


    N = topics.__len__()

    print('value of N:/n')
    print(N)

    for i in topics:
        print(i)
        siteType = SiteType.objects.get_or_create(type=i)[0]
    print(siteType)


def populate(N):
    '''
    Create N Entries of Dates Accessed
    '''
    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()
        fake_date = fakegen.date()
        fake_websitename = fakegen.url()

        sitetypeAll = SiteType.objects.all()

        sitetypeSel = random.choice(sitetypeAll)

        print(sitetypeSel)

        # print(sitetype)

        user = AppUser.objects.get_or_create(name=fake_first_name,
                                            surname=fake_last_name,
                                            email=fake_email)[0]

        web = Website.objects.get_or_create(sitetype=sitetypeSel,
                                            url=fake_websitename)[0]

        activity = UserActivities.objects.get_or_create(appUser=user,
                                                        webstVisited=web,
                                                        date=fake_date)[0]

if __name__ == '__main__':


    populateSiteTypes()

    print("Populating the databases...Please Wait")

    populate(10)

    print('Populating Complete')
