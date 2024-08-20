from django import forms
from .models import Booking, Menu

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email', 'booking_date', 'booking_time', 'additional_info']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'small_price', 'large_price', 'image']
