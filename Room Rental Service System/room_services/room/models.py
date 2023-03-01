from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=20,null=True)
    dob = models.CharField(max_length=30,null=True)
    def _str_(self):
        return self.user.username

class Feedback(models.Model):
    fname = models.CharField(max_length=20,null=True)
    femail = models.CharField(max_length=20,null=True)
    fcontact = models.CharField(max_length=20,null=True)
    feedback = models.CharField(max_length=30,null=True)

class Room(models.Model):
    room_no = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    type = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True)


class Booking(models.Model):
    room_no = models.CharField(max_length=20,null=True)
    fullname = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    contact1 = models.CharField(max_length=30,null=True)
    contact2 = models.CharField(max_length=30,null=True)
    booking_date = models.CharField(max_length=30,null=True)
    days = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length=30,null=True)
    price = models.CharField(max_length=30,null=True)
    dob = models.CharField(max_length=30,null=True)
    status = models.CharField(max_length=30,null=True)

