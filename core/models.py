from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=100)
    small_price = models.DecimalField(max_digits=10, decimal_places=2)
    large_price = models.DecimalField(max_digits=10, decimal_places=2)
    image =models.ImageField(upload_to = 'image/menu/')
    
    def __str__(self):
        return self.name

class About(models.Model):
    DetailsAboutUs = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.DetailsAboutUs
    
class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    
    def __str__(self):
        return self.email
    
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.customer_name} on {self.booking_date} at {self.booking_time}"