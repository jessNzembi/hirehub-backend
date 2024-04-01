from django.urls import path
from .views import signup, log_in, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', logout_view, name='logout'),
]
