from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ContactModel,diettrack
# Create your views here.

def Home(request):
    return render(request,"index.html")


# views.py
def contact(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        usernumberr = request.POST.get('usernumberr')

        print(f"Username: {username}, Email: {email}, Phone: {usernumberr}")

        if not usernumberr or len(usernumberr) != 10:
            messages.info(request, "Phone number must be 10 digits.")
            return redirect("contact")

        # Save to ContactModel
        contact = ContactModel(n_ame=username, e_mail=email, p_hone=usernumberr)
        contact.save()

        print("Contact saved successfully.")

        # Create user
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username is already registered")
            return redirect('contact')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already registered")
            return redirect('contact')

        myuser = User.objects.create_user(username=username, email=email, password='defaultpassword')
        myuser.save()

        print("User created successfully.")

        messages.success(request, "Congratulations! User is created")
        return redirect("contact")

    return render(request, "contact.html")

def portfolio(request):
    if request.method == "POST":
        date = request.POST.get('date')
        meal = request.POST.get('meal')
        calories = request.POST.get('calories')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        waterintake = request.POST.get('waterintake')
        notes = request.POST.get('notes')

        # Debugging output to verify the values being passed
        print(f"date: {date}, meal: {meal}, calories: {calories}, height: {height}, weight: {weight}, waterintake: {waterintake}, notes: {notes}")

        # Create and save the diettrack entry
        diet_entry = diettrack(
            d_ate=date,
            meal=meal,
            calories=calories,
            height=height,
            weight=weight,
            waterintake=waterintake,
            notes=notes
        )
        diet_entry.save()

        messages.success(request, "Diet entry successfully saved!")
        return redirect('portfolio')

    return render(request, "portfolio.html")

def services(request):
    return render(request, 'services.html')