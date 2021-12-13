from django.urls import path
from .views import create_meeting, get_meetings, get_user_details, home, generate_access_token
urlpatterns = [
    path('/', home),
    path('token/', generate_access_token),
    path('create/', create_meeting),
    path('get_meetings/', get_meetings)
]