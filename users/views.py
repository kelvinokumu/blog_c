from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# This view handles user registration
def register_view(request):
    # Check if the request is a POST (form submission)
    if request.method == "POST":
        # Create a form instance with the submitted data
        form = UserCreationForm(request.POST)
        
        # Validate the form data
        if form.is_valid():
            # Save the new user to the database
            form.save()
            # Redirect to the "posts" list page after successful registration
            return redirect("posts:list")
    else:
        # If not a POST request, display a blank registration form
        form = UserCreationForm()
    
    # Render the registration page with the form
    return render(request, "users/register.html", {"form": form})
