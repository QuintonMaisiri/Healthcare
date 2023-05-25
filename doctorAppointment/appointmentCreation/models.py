from django.db import models

# Create your models here.

class Account(models.Model):
    TYPE =[
        ("D","DOCTOR"),
        ("A","ADMIN"),
        ("P","PATIENT")
    ]
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    type = models.CharField(max_length=8, choices=TYPE)

class Person(models.Model):
    GENDER = [
        ("F","FEMALE"),
        ("M","MALE")
    ]
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    gender = models.CharField(max_length=1,choices=GENDER)
    username = models.OneToOneField(Account,on_delete= models.CASCADE)

class Next_of_kin(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)

class Patient(Person, models.Model):
    address = models.CharField(max_length=64)
    next_of_kin = models.OneToOneField(Next_of_kin,on_delete= models.CASCADE)

class Doctor(Person , models.Model):
    pass

class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    details = models.TextField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)


class Review(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    rating = models.IntegerField()
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    comment = models.TextField()