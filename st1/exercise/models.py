from django.db import models

class AppUser(models.Model):
    name = models.CharField(max_length=264,unique=True)
    surname = models.CharField(max_length=264,unique=True)
    email = models.EmailField(max_length=70,blank=True)
    def __str__(self):
        return str(self.name +" "+self.surname)


class UserActivities(models.Model):
    appUser = models.ForeignKey(AppUser,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(date)


class ActivityType(models.Model):
    pass
