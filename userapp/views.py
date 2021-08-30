from django import forms
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from .models import User
from store.models import Customer, Order


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            # email = form.cleaned_data.get('email')
            # password = form.cleaned_data.get('password')
            # print(type(form.changed_data[1]))
            # user = User.objects.create(email=email,password=password, user_type=form.cleaned_data['user_type'])
            # user.save()
            user = form.save()
            # get_in_user = authenticate(email=email, password=password)
            login(request, user)
            user = request.user
            customer = Customer.objects.create(user=user,name=user.get_full_name())
            customer.save()
            order = Order.objects.create(customer=customer, complete=False)
            order.save()
            return redirect('store:store')
    else:
        form = UserRegisterForm()
    return render(request, 'userapp/register.html', {'form': form})
