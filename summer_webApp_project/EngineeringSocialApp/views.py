from django.shortcuts import render, redirect
# Create your views here.

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
    return render(request, 'login.html', {'form': form})
def home(request):
    return render(request, 'home.html')
