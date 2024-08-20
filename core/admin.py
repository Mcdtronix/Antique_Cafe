from django.contrib import admin
from . models import Menu,About,Contact,Booking

# Register your models here.
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name','small_price', 'large_price']
    
    
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['DetailsAboutUs']
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['address', 'email', 'tel']
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'booking_date','booking_time','additional_info']