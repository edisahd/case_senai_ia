from django.urls import path
from authentication.views import LoginView, RenovateView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('renovate/', RenovateView.as_view()),
    path('logout/', LogoutView.as_view()),
]