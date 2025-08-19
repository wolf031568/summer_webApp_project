from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from users.models import Users
# Create your views here.
#this is using djangos built in authentication system
def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    #Django’s login form is returned using the POST method, in which the browser bundles up the form data, 
    #encodes it for transmission, sends it to the server, and then receives back its response.
    #handle post request
    if request.method == "POST":
        #get user information from the form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #login user
                auth_login(request, user)
                return redirect('home')
    return render(request, 'users/login.html', {'form': form})

#registration for django
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, password=password)
            # create the corresponding Users object
            Users.objects.create(user=user)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    return render(request, 'users/register.html')

#bulletin board view
def bulletin_board(request):
    return render(request, 'bulletin_board.html')

#home view
@login_required
def home(request):
    custom_user, created = Users.objects.get_or_create(user=request.user)
    return render(request, 'home.html', {"custom_user": custom_user})

#edit profile view
@login_required
def edit_profile(request):
    custom_user = Users.objects.get(user=request.user)

    if request.method == "POST":
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.email = request.POST.get("email")
        request.user.save()

        custom_user.major = request.POST.get("major")
        custom_user.phone = request.POST.get("phone")  # optional
        custom_user.save()

        return redirect("home")

    return render(request, "edit_profile.html", {"custom_user": custom_user})

#logout view triggers an authentication logout then redirects to the login page
@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')  # Redirect to your login page