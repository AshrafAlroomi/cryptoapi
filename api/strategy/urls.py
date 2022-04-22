from django.urls import path
from .views import StrategyView, StrategiesView

urlpatterns = [
    path('stratgy/', StrategyView.as_view(), name='stratgy'),
    path('stratgies/', StrategiesView.as_view(), name='stratgies'),
]
