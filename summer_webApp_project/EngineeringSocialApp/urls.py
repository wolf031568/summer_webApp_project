from django.urls import path
from . import views

#all the urls the main app will use, login and registration are in users.urls
urlpatterns = [
    path('', views.home, name='home'),  # Home page (requires login)
    path('login/', views.login_view, name='login'),  # Login page
    path('register/', views.register_view, name='register'),  # Registration page
    path('edit_profile/', views.edit_profile, name='edit_profile'),  # Edit profile
    path('bulletin_board/', views.bulletin_board, name='bulletin_board'),  # Bulletin board
    path('logout/', views.logout_view, name='logout'),  # Logout
]