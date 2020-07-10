from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snippets/', include('app.snippets.urls')),
    path('examinator/', include('app.examinator.urls')),
]
