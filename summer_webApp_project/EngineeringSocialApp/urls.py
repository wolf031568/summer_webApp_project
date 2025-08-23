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
    path('bulletin/', views.bulletin_board, name='bulletin_board'),
    path('bulletin/add/', views.add_event, name='add_event'),
    path('bulletin/edit/<int:pk>/', views.edit_event, name='edit_event'),
    path('bulletin/delete/<int:pk>/', views.delete_event, name='delete_event'),
    path('calendar/', views.event_calendar, name='event_calendar'),
    path('emergency/', views.emergency_contacts, name='emergency_contacts'),
    path('search/', views.search_users, name='search_users'),
    path('profile/<int:user_id>/', views.public_profile, name='public_profile'),
    
]