from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

 

# from django.contrib.auth import User
# Create your models here.

class Slot(models.Model):
    start_time=models.CharField(max_length=20,default=1)
    end_time=models.CharField(max_length=20,default=1)
    def __str__(self):
        return self.start_time + " To " + self.end_time
    
class Ground(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=10)
    ground_description=models.CharField(max_length=300,default=" ")
    def __str__(self):
        return self.name

class MyUsers(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_user = models.CharField(max_length=15,default=1)
    email = models.EmailField('User Mail',blank=True)
    def __str__(self):
        return self.first_name + " " + self.last_name


class Booking(models.Model):
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    book_date=models.DateField()
    venue = models.ForeignKey(Ground,blank=True,null=True,on_delete=models.CASCADE)
     
    slot = models.ForeignKey(Slot,blank=True,null=True,on_delete=models.CASCADE)
    description= models.TextField(blank=True)
    attendees=models.ManyToManyField(MyUsers,blank=True)
    def __str__(self):
        return self.name

# class Cancellation(models.Model):

class Rating(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUsers, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField()

    def __str__(self):
        return f"Rating for {self.booking.name} by {self.user.first_name} "