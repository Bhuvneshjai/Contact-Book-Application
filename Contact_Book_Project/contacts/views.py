from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            return redirect('contact',name=name)
    return render(request, 'contacts/home.html')

def contact(request, name):
    if request.method == 'POST':
        # Handle adding or updating a contact
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        action = request.POST.get('action')

        if action == 'delete':
            contact = get_object_or_404(Contact, email=email)
            contact.delete()
        else:
            Contact.objects.update_or_create(
                email=email,
                defaults={'name': name, 'phone': phone, 'address': address},
            )
        return redirect('contact', name=name)
    
    # Fetch all contacts
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact.html', {'name': name, 'contacts': contacts})

def display(request, email):
    contact = get_object_or_404(Contact, email=email)
    return render(request, 'contacts/display.html', {'contact': contact})

def logout(request):
    return HttpResponseRedirect('/')

