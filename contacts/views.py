from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
        # Extract common fields from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', None)
        message = request.POST.get('message', None)
        
        # Determine if the user is authenticated
        user_id = request.user.id if request.user.is_authenticated else None

        # Attempt to assign listing_id or landlisting_id if provided
        listing_id = request.POST.get('listing_id', None)
        landlisting_id = request.POST.get('landlisting_id', None)
        
        # Determine if this is a property or land listing based on provided IDs
        listing_type = 'land' if landlisting_id else ''
        listing_reference_id = landlisting_id if landlisting_id else listing_id
        listing_title = request.POST.get('listing', email) or request.POST.get('landlisting', email)

        if listing_reference_id:
            try:
                listing_reference_id = int(listing_reference_id)
            except ValueError:
                messages.error(request, "Invalid listing ID.")
                return redirect('contacts:contact')

        # Create and save the Contact object
        new_contact = Contact(
            name=name, 
            email=email, 
            phone=phone, 
            message=message, 
            user_id=user_id,
            listing_id=listing_reference_id,  # Use the same field for both listing types for simplicity
            landlisting_id=landlisting_id,
            listing=listing_title
        )
        new_contact.save()

        # Prepare and send the email notification
        email_subject = f'{listing_type.capitalize()} Listing Inquiry'
        admin_url = 'https://abn-realtors.onrender.com/admin/'  # Local admin URL
        email_body = (
            f'{listing_title}.\n'
            f'There has been an inquiry. Sign into the admin panel for more info.\n'
            f'Admin Panel: {admin_url}.\n'
            f'{new_contact.message}'
            
        )

        send_mail(
            email_subject,
            email_body,
            'abnrealtorsgroup@gmail.com',
            ['chinemeremokpara93@gmail.com', 'okpechichinedum@gmail.com'],
            fail_silently=True
        )

        messages.success(request, 'Your request has been submitted. Log in to view listings.')

        # Redirect logic after saving the contact
        return redirect(f'/{listing_type}listings/{listing_reference_id}' if listing_reference_id else 'contacts:contact')

    else:
        return render(request, 'contacts/contacts.html')
