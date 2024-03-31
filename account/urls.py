from django.urls import path

from account.views import login, logout, profile, registration

app_name = 'account'
urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),

]