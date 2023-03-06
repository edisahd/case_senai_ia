from django.urls import path
from prediction.views import PredictionLimitedView, PredictionResourceView, PredictionView

urlpatterns = [
    path('', PredictionView.as_view()),
    path('<int:id>/', PredictionResourceView.as_view()),
    path('<int:limit>/<int:offset>/', PredictionLimitedView.as_view()),
]