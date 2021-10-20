from django.urls import path

from ussd.views import HandleUssd, HandleEvent

urlpatterns = [
    path('handle_ussd/', HandleUssd.as_view()),
    path('handle_event/',HandleEvent.as_view())
]
