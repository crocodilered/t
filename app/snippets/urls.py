from django.urls import path
from .views import FormView, SnippetGeneralView, SnippetLatestView


urlpatterns = [
  path('', SnippetGeneralView.as_view(), name='snippet_post'),
  path('<int:snippet_pk>/', SnippetGeneralView.as_view(), name='snippet_retrieve'),
  path('latest/', SnippetLatestView.as_view(), name='latest'),
  path('form/', FormView.as_view(), name='form'),
]
