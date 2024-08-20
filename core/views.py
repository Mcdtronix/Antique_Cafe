from django.shortcuts import redirect, render
from . models import Menu,About,Contact,Booking
from django.core.mail import send_mail
from .forms import BookingForm, MenuForm 

# Create your views here.
from .forms import BookingForm

def home(request):
    menus = Menu.objects.all()
    abouts = About.objects.all()
    contacts = Contact.objects.all()
    
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('home')  # Redirect after POST to prevent duplicate submissions
    else:
        booking_form = BookingForm()

    context = {
        'menus': menus,
        'abouts': abouts,
        'contacts': contacts,
        'booking_form': booking_form,
    }
    return render(request, "index.html", context)


def manager_dashboard(request):
    bookings = Booking.objects.all()

    if request.method == 'POST':
        if 'add_menu_item' in request.POST:
            menu_form = MenuForm(request.POST, request.FILES)
            if menu_form.is_valid():
                menu_form.save()
                return redirect('manager_dashboard')

        elif 'reply_to_booking' in request.POST:
            booking_id = request.POST.get('booking_id')
            reply_message = request.POST.get('reply_message')
            booking = Booking.objects.get(id=booking_id)
            send_mail(
                'Your Booking Response',
                reply_message,
                'kudakwashemacdonald16@gmail.com',  # Replace with your email
                [booking.customer_email],
                fail_silently=False,
            )
            return redirect('manager_dashboard')

    else:
        menu_form = MenuForm()

    context = {
        'menu_form': menu_form,
        'bookings': bookings,
    }
    return render(request, 'manager_dashboard.html', context)
