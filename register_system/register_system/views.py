from django.shortcuts import render, redirect
from .models import Users

def home(request):
    return render(request, 'home.html')
    
def user_create(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if Users.objects.filter(email=email).exists():
            error_message = "Um usuário com este e-mail já está registrado."
            users_list = Users.objects.all()  
            return render(request, 'Users.html', {'error_message': error_message, 'users': users_list})
        
        if Users.objects.filter(password=password).exists():
            error_message = "A senha já está associada a outro usuário."
            users_list = Users.objects.all()  
            return render(request, 'Users.html', {'error_message': error_message, 'users': users_list})
        
        novo_user = Users(email=email, password=password)
        novo_user.save()

        return redirect('user_create')
    
    users_list = Users.objects.all()
    return render(request, 'Users.html', {'users': users_list})