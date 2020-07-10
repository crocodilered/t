from django.urls import path
from .views import MainView


urlpatterns = [
  path('', MainView.as_view(), name='create'),
  path('<int:exec_id>/', MainView.as_view(), name='retrieve'),
]
