from django.urls import path
from .views import delete_user, signup, log_in, logout_view, get_user, profile_create, profile_detail, update_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', logout_view, name='logout'),
    path('delete/<int:user_id>', delete_user),
    path('users/<int:user_id>/', get_user),
    path('profiles/<int:user_id>/', profile_detail),
    path('profiles/create/', profile_create),
    path('profiles/update/<int:user_id>/', update_profile)
]
