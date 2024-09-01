from django.shortcuts import redirect, render, get_object_or_404
from . models import Menu,About,Contact,Booking
from django.core.mail import send_mail
from .forms import BookingForm, MenuForm 
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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




@login_required
def manager_dashboard(request): 
    bookings = Booking.objects.all()
    menus = Menu.objects.all()
    menu_form = MenuForm() 

    if request.method == 'POST':
        if 'add_menu_item' in request.POST:
            menu_form = MenuForm(request.POST, request.FILES)
            if menu_form.is_valid():
                menu_form.save()
                messages.success(request, 'Menu item added successfully!')
                return redirect('manager_dashboard')

        elif 'update_menu_item' in request.POST:
            menu_item_id = request.POST.get('menu_item_id')
            menu_item = get_object_or_404(Menu, id=menu_item_id)
            form = MenuForm(request.POST, request.FILES, instance=menu_item)
            if form.is_valid():
                form.save()
                messages.success(request, 'Menu item updated successfully!')
                return redirect('manager_dashboard')

        elif 'delete_menu_item' in request.POST:
            menu_item_id = request.POST.get('menu_item_id')
            menu_item = get_object_or_404(Menu, id=menu_item_id)
            menu_item.delete()
            messages.success(request, 'Menu item deleted successfully!')
            return redirect('manager_dashboard')

        elif 'reply_to_booking' in request.POST:
            booking_id = request.POST.get('booking_id')
            reply_message = request.POST.get('reply_message')
            booking = Booking.objects.get(id=booking_id)
            send_mail(
                'Your Booking Response',
                reply_message,
                'your-email@example.com',  # Replace with your email
                [booking.customer_email],
                fail_silently=False,
            )
            messages.success(request, 'Reply sent successfully!')
            return redirect('manager_dashboard')

    else:
        menu_form = MenuForm()

    context = {
        'menus': menus,
        'menu_form': menu_form,
        'bookings': bookings,
    }
    return render(request, 'manager_dashboard.html', context)

# View to update a menu item
def update_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard')  # Redirect to the manager dashboard after saving
    else:
        form = MenuForm(instance=menu)
    
    return render(request, 'update_menu.html', {'form': form})

# View to delete a menu item
def delete_menu(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    
    if request.method == "POST":
        menu.delete()
        return redirect('manager_dashboard')  # Redirect to the manager dashboard after deletion
    
    return render(request, 'delete_menu.html', {'menu': menu})

