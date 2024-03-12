from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.ImageField(upload_to='donor',null=True, blank=True)
    regdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username


class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.ImageField(upload_to='volunteer',null=True,blank=True)
    idpic = models.ImageField(upload_to='volunteer',null=True, blank=True)
    aboutme = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=20,null=True)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300,null=True)
    updationdate = models.DateField(null=True)

    def __str__(self):
        return self.user.username
    
class DonationArea(models.Model):
    areaname = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname
    
DONATION_CHOICES={
    ('Food Donation', 'Food Donation'),
    ('Cloth Donation', 'Cloth Donation'),
    ('Footware Donation', 'Footwear Donation'),
    ('Books Donation', 'Books Donation'),
    ('Furniture Donation', 'Furniture Donation'),
    ('Vessel Donation', 'Vessel Donation'),
    ('other', 'other'),
}

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donationname = models.CharField(choices=DONATION_CHOICES,max_length=100,null=True)
    donationpic = models.ImageField(upload_to='donation',null=True, blank=True)
    collectionloc = models.CharField(max_length=300,null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=30,null=True)
    donationdate = models.DateField(null=True)
    adminremark = models.CharField(max_length=200,null=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE,null=True)
    donationarea = models.ForeignKey(DonationArea, on_delete=models.CASCADE,null=True)
    volunteerremark = models.CharField(max_length=200,null=True)
    updationdate = models.DateField(null=True)
    documentation = models.DateField(default=date.today)

    def __str__(self):
        return self.id
    

class Gallery(models.Model):
    donation = models.ForeignKey(Donation, on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id