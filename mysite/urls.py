from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),  # Ensure this is correctly importing 'polls.urls'
    path('admin/', admin.site.urls),
]
