from django.shortcuts import render, redirect
from .forms import SignUpForm 
from django.views.generic import View
from django.contrib import messages

class SignUpView(View):
    def get(self, request):
        context = {
            'form':SignUpForm()
        }
        return render(request, 'registration/signup.html', context)
    

    def post(self, request):
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are successfully created")
            return redirect('login')
        return render(request, 'registration/signup.html', {'form': form})
